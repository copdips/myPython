import asyncio

import aiomysql


async def main():
    # 新建一个db链接
    conn = await aiomysql.connect(
        host="127.0.0.1", port=3306, user="root", password="12345", db="mysql"
    )
    # 得到一个游标
    cur = await conn.cursor()
    ret = await cur.execute("select host, user from user")
    print(ret)  # 影响到的行数/查询结果的行数

    print(await cur.fetchone())

    # 获得多有结果的函数
    rets = await cur.fetchall()
    print(rets)

    await cur.close()
    conn.close()


asyncio.run(main())
