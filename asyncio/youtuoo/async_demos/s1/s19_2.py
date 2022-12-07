import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def download_img(url):
    print(f"下载图片：{url}")
    time.sleep(1)
    print(f"下载完成：{url}")


async def main():
    executor = ThreadPoolExecutor(2)

    loop = asyncio.get_running_loop()
    tasks = []
    for i in range(10):
        t = loop.run_in_executor(executor, download_img, i)
        tasks.append(t)

    await asyncio.wait(tasks)


asyncio.run(main())
