import time


def download_img(url):
    print(f"下载图片：{url}")
    time.sleep(1)
    print(f"下载完成：{url}")


def main():
    for i in range(10):
        download_img(i)


main()
