import time
from concurrent.futures import ThreadPoolExecutor


def download_img(url):
    print(f"下载图片：{url}")
    time.sleep(1)
    print(f"下载完成：{url}")


def main():
    executor = ThreadPoolExecutor(3)
    for i in range(10):
        executor.submit(download_img, i)


main()
