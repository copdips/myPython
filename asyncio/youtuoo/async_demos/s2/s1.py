# f = open("test.txt", "w")
# f.write("asdadad")
# f.close()
#
#
# with open("test.txt", "w") as f:
#     f.write("asasas")

# __enter__ 、__exit__


import time


class ContextManager:
    def __init__(self):
        self.conn = None

    def action(self):
        return self.conn

    def __enter__(self):
        # 链接数据库
        print("开始连接")
        time.sleep(1)
        self.conn = "OK"
        return self  # self

    def __exit__(self, exc_type, exc, tb):
        # 关闭数据库链接
        print("关闭连接")
        self.conn = "CLOSE"


def main():
    with ContextManager() as cm:
        result = cm.action()
        print(result)

    print(111)


main()
