# pip install aiohttp
import asyncio

import aiohttp


async def fetch(session, url):
    async with session.get(url, verify_ssl=False) as response:
        text = await response.text()
        print(f"Got response: {url}, {len(text)}")
        return text


async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            "https://python.org",
            "https://www.baidu.com",
            "https://www.pythonav.com",
        ]
        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]
        done, pending = await asyncio.wait(tasks)


if __name__ == "__main__":
    asyncio.run(main())
