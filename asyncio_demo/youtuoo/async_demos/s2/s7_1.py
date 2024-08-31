import asyncio
from email.message import EmailMessage

import aiosmtplib


async def main():
    message = EmailMessage()

    message["From"] = "root@localhost"
    message["To"] = "xxx@qq.com"
    message["Subject"] = "这是一个邮件主题"

    message.set_content("这是一个测试邮件，请忽略")

    await aiosmtplib.send(
        message,
        hostname="smtp.qq.com",
        port=587,
        username="你的QQ邮箱号",
        password="授权码",
    )


asyncio.run(main())
