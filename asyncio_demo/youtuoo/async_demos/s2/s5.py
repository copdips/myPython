import asyncio

import aiohttp
import httpx


async def aiohttp_demo():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://www.baidu.com") as response:
            print(response.status)  # 响应状态码
            html = await response.text()
            print(html)


async def httpx_demo():
    async with httpx.AsyncClient() as client:
        resp = await client.get("http://www.baidu.com")
        print(resp.status_code)
        print(resp.text)


# asyncio.run(aiohttp_demo())
asyncio.run(httpx_demo())
