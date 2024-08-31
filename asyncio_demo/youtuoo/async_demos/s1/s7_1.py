import asyncio

import aiohttp


async def download_img(session, url):
    file_name = url.rsplit("/")[-1]
    print(f"下载图片：{file_name}")
    await asyncio.sleep(2)
    response = await session.get(url, ssl=False)
    content = await response.content.read()
    with open(file_name, mode="wb") as file:
        file.write(content)
    print(f"下载完成：{file_name}")


async def main():
    urls = [
        "https://tenfei05.cfp.cn/creative/vcg/800/new/VCG41560336195.jpg",
        "https://tenfei03.cfp.cn/creative/vcg/800/new/VCG41688057449.jpg",
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(download_img(session, url)) for url in urls]
        await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
