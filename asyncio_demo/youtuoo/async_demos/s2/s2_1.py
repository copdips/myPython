# __aiter__  __anext__
import asyncio


class AsyncMyRange:
    def __init__(self, total=0):
        self.total = total
        self.count = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.count < self.total:
            await asyncio.sleep(1)
            x = self.count
            self.count += 1
            return x
        else:
            raise StopAsyncIteration


async def main():
    async for i in AsyncMyRange(10):
        print(i)


asyncio.run(main())
