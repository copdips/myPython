import asyncio


# 协程函数
async def f1():
    print(123)
    print(456)


# 协程对象
# print(f1())

asyncio.run(f1())
