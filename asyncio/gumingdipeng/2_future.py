# https://www.cnblogs.com/traditional/p/17363960.html

import asyncio

# asyncio 里面有一个类 Future，实例化之后即可得到 future 对象
# 然后 asyncio 里面还有一个类 Task，实例化之后即可得到 task 对象（也就是任务）
# 这个 Task 是 Future 的子类，所以我们用的基本都是 task 对象，而不是 future 对象
# 但 Future 这个类和 asyncio 的实现有着密不可分的关系，所以我们必须单独拿出来说一说

future = asyncio.Future()
print(future)  # <Future pending>
print(future.__class__)  # <class '_asyncio.Future'>
print(f"future 是否完成: {future.done()}")  # future 是否完成: False

# 设置一个值，通过 set_result
future.set_result("古明地觉")
print(f"future 是否完成: {future.done()}")  # future 是否完成: True
print(future)  # <Future finished result='古明地觉'>
print(f"future 的返回值: {future.result()}")  # future 的返回值: 古明地觉
