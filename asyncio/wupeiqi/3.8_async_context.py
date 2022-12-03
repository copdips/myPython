import asyncio


class AsyncContextManager:
    def __init__(self):
        print("AsyncContextManager init")
        self.conn = None

    async def do_something(self):
        return 666

    async def __aenter__(self):
        print("AsyncContextManager __aenter__ in")
        self.conn = await asyncio.sleep(1)
        print("AsyncContextManager __aenter__ out")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("AsyncContextManager __aexit__ in")
        await asyncio.sleep(1)
        print("AsyncContextManager __aexit__ out")


async def func():
    async with AsyncContextManager() as acm:
        result = await acm.do_something()
        print(result)


asyncio.run(func())
