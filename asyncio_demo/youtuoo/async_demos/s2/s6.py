import asyncio

from aiofile import async_open


async def main():
    async with async_open("test.txt", "w+") as afp:
        await afp.write("Hello ")
        await afp.write("world")
        afp.seek(0)

        print(await afp.read())

        await afp.write("heee\nee\nee")
        afp.seek(0)

        print(await afp.readline())
        print(await afp.readline())
        print(await afp.readline())


asyncio.run(main())
