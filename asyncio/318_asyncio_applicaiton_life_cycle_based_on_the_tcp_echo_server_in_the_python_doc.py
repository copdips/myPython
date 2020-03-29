from asyncio import (
    get_event_loop,
    start_server,
    CancelledError,
    StreamReader,
    StreamWriter,
    Task,
    gather,
)


async def echo(reader: StreamReader, writer: StreamWriter):
    print("New connection.")
    try:
        while True:
            data: bytes = await reader.readline()
            if data in [b"", b"quit"]:
                break
            writer.write(data.upper())
            await writer.drain()
        print("Leaving Connection.")
    # except CancelledError:
    #     # don't create any new tasks inside this exception handler
    #     # as Task.all_tasks() wont be aware of them.
    #     writer.write_eof()
    #     print('Cancelled')
    finally:
        writer.close()


loop = get_event_loop()
coro = start_server(echo, "127.0.0.1", 8888, loop=loop)
server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    print("Shutting down!")

server.close()
loop.run_until_complete(server.wait_closed())

tasks = Task.all_tasks()
for t in tasks:
    t.cancel()

# return_exception=True to let group handle the subtasks' exceptions
# as returned values, so that they don’t
# bubble out and interfere with run_until_complete()
group = gather(*tasks, return_exceptions=True)
loop.run_until_complete(group)
loop.close()
