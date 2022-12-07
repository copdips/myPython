import asyncio


class ContextManager:
    def __init__(self):
        self.conn = None

    async def action(self):
        return self.conn

    async def __aenter__(self):
        # 链接数据库
        print("开始连接")
        await asyncio.sleep(1)
        self.conn = "OK"
        return self  # self

    async def __aexit__(self, exc_type, exc, tb):
        # 关闭数据库链接
        print("关闭连接")
        self.conn = "CLOSE"


async def main():
    async with ContextManager() as cm:
        result = await cm.action()
        print(result)

    print(111)


asyncio.run(main())
