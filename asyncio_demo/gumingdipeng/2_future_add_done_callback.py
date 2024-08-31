import asyncio


def callback(future):
    print(f"future 已完成，值为 {future.result()}")


async def main():
    future = asyncio.Future()
    # 绑定一个回调，当 future 有值时会自动触发回调的执行
    future.add_done_callback(callback)
    future.set_result("666")


asyncio.run(main())
"""
future 已完成，值为 666
"""
