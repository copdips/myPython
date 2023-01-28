# wrap requests.get into asyncio
import asyncio

import requests


async def download_image(url):
    print(f"Downloading: {url}")
    loop = asyncio.get_running_loop()
    # ! requests module doesn't support asyncio, so we use it in thread pool, and wrap it into a asyncio.Future
    # ! the result will be the same with asyncio natively compatible aiohttp, but here with run_in_executor(),
    # ! we must create multiple thread which takes more resource and so less efficient.
    # TODO: check 5.4_crawler.py to see how to use aiohttp to do the same thing.
    response = await loop.run_in_executor(None, requests.get, url)
    print(f"Downloaded: {url}")

    file_name = url.split("/")[-1]
    with open(file_name, mode="wb") as file_object:
        file_object.write(response.content)


if __name__ == "__main__":
    url_list = [
        "https://github.com/copdips/copdips.github.io/blob/main/_image/blog/2022-03-27-manage-azure-databricks-service-principal/azure-databricks-multiple-workspaces.png",
        "https://github.com/copdips/copdips.github.io/blob/main/_image/blog/2018-05-26-grep-like-powershell-colorful-select-string/powershell7-default-highlighting.png",
    ]
    # cannot use asyncio.create_task() here, becasue there's no running event loop yet, which will be created by below asyncio.get_event_loop()
    # so we must create coroutine and then concert it to Future by asyncio.wait()
    tasks = [download_image(url) for url in url_list]
    # ! asyncio.ensure_future() is not necessary
    # tasks = [asyncio.ensure_future(download_image(url)) for url in url_list]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
