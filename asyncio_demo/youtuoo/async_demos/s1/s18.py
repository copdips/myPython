import time
from concurrent.futures import Future, ThreadPoolExecutor


def task(a, b):
    time.sleep(2)
    return a + b


def callback(f: Future):
    print(f.result())


pool = ThreadPoolExecutor(5)  # 生成一个线程池，大小为5

print("开始了")
for i in range(5):
    pool.submit(task, i, i).add_done_callback(callback)
    # 异步执行，绑定回调函数获取结果

print("结束了")
