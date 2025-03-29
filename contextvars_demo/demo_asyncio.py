# https://docs.python.org/3/library/contextvars.html#asyncio-support
import asyncio
import contextvars

client_addr_var = contextvars.ContextVar("client_addr")


def render_goodbye():
    # The address of the currently handled client can be accessed
    # without passing it explicitly to this function.

    client_addr = client_addr_var.get()
    return f"Good bye, client @ {client_addr}\r\n".encode()


async def long_task(new_value):
    client_addr_var.set(new_value)
    await asyncio.sleep(0.1)
    client_addr = client_addr_var.get()
    print(f"Long task for client @ {client_addr}")
    return f"Long task for client @ {client_addr}\r\n".encode()


async def handle_request(reader, writer):
    addr = writer.transport.get_extra_info("socket").getpeername()
    client_addr_var.set(addr)

    # In any code that we call is now possible to get
    # client's address by calling 'client_addr_var.get()'.

    while True:
        line = await reader.readline()
        print(line)
        if not line.strip():
            break

    # await long_task("simple_await") just runs the coroutine in the same Task as the caller, so the same context is preserved.
    # No new context is created
    # Any changes to context variables affect the caller's context.
    # It's like making a regular function call, just asynchronously
    await long_task("simple_await")

    # asyncio.create_task creates new tasks, so the context is not preserved.
    # Each new Task gets its own copy of the current context at creation time.
    # Changes to context variables in one Task don't affect other Tasks.
    # It's like spawning a separate thread of execution (but still on the same OS thread).
    tasks = [asyncio.create_task(long_task("with_gather")) for _ in range(2)]
    res = await asyncio.gather(*tasks)
    print(f"res: {res}")

    writer.write(b"HTTP/1.1 200 OK\r\n")  # status line
    writer.write(b"\r\n")  # headers
    writer.write(render_goodbye())  # body
    writer.close()


async def main():
    srv = await asyncio.start_server(handle_request, "127.0.0.1", 8081)

    async with srv:
        await srv.serve_forever()


asyncio.run(main())

# To test it you can use telnet or curl:
#     telnet 127.0.0.1 8081
#     curl 127.0.0.1:8081
