import time

import requests


def download_img(url):
    file_name = url.rsplit("/")[-1]
    print(f"下载图片：{file_name}")
    time.sleep(2)
    response = requests.get(url)
    with open(file_name, mode="wb") as file:
        file.write(response.content)
    print(f"下载完成：{file_name}")


def main():
    urls = [
        "https://tenfei05.cfp.cn/creative/vcg/800/new/VCG41560336195.jpg",
        "https://tenfei03.cfp.cn/creative/vcg/800/new/VCG41688057449.jpg",
    ]
    for item in urls:
        download_img(item)


main()
