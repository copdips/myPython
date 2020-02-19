import asyncio


async def f():
    pass


coro = f()

# create_task() only accepts coroutine and needs a event loop object, it returns a asyncio.Task object.
loop = asyncio.get_event_loop()
task = loop.create_task(coro)
assert isinstance(task, asyncio.Task)

# ensure_future tasks either coroutine or future, and doesn't need the event loop instance, but ensure_future is often used by framework developer, not a framework user like me.
new_task = asyncio.ensure_future(coro)
assert isinstance(new_task, asyncio.Task)

# if inject an already asyncio.Task to ensure_future(), the function does nothing, just return the same input as output.
mystery_meat = asyncio.ensure_future(task)
assert mystery_meat is task


async def background_job():
    pass


async def option_a(loop):
    loop.create_task(background_job())


async def option_b():
    asyncio.ensure_future(background_job())


# * asyncio.create_task() already exists in one of the python3.7 or 3.8
async def option_c():
    loop = asyncio.get_event_loop()
    loop.create_task(background_job())

loop = asyncio.get_event_loop()

loop.create_task(option_a(loop))
loop.create_task(option_b())
loop.create_task(option_c())


if __name__ == "__main__":
    pass