"""
he implicit context switching only happens at await points to preserve the context across potential task switches.
But this isn't creating a new isolated context - it's preserving the existing context.
"""

import asyncio
import contextvars

# Create a context variable
request_id = contextvars.ContextVar("request_id")
request_id.set("default")


async def process_request(req_id):
    # Set the context variable for this task
    request_id.set(req_id)
    print(f"Task {req_id} started with request_id = {request_id.get()}")

    # This await point causes an implicit context switch
    # The current context is saved
    await asyncio.sleep(0.5)

    # When execution returns, the context is restored automatically
    print(f"Task {req_id} after first await: request_id = {request_id.get()}")

    # Do some more work and switch again
    await asyncio.sleep(0.1)

    # Context is still preserved
    print(f"Task {req_id} finished: request_id = {request_id.get()}")

    # Call a regular function - sharing the same context
    helper_function(req_id)

    return f"Completed {req_id}"


def helper_function(req_id):
    # This function shares the context of its caller
    # It's not a new context, just accessing the existing one
    current_id = request_id.get()
    print(f"Helper function {req_id} sees: request_id = {current_id}")


async def main():
    # Start two tasks concurrently
    print(f"Main start: request_id = {request_id.get()}")

    # await process_request("request-0") just runs the coroutine in the same Task
    # as the caller, so the same context is preserved.
    # No new context is created
    # Any changes to context variables affect the caller's context.
    # It's like making a regular function call, just asynchronously
    await process_request("request-0")

    # asyncio.create_task creates new tasks, so the context is not preserved.
    # Each new Task gets its own copy of the current context at creation time.
    # Changes to context variables in one Task don't affect other Tasks.
    # It's like spawning a separate thread of execution (but still on the same OS thread).
    tasks = [
        asyncio.create_task(process_request("request-1")),
        asyncio.create_task(process_request("request-2")),
    ]

    # Wait for both tasks to complete
    results = await asyncio.gather(*tasks)
    print(results)

    print(f"Main end: request_id = {request_id.get()}")


asyncio.run(main())
