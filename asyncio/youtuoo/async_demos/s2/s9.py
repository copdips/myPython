# 方式1
import asyncio

import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


loop = asyncio.get_event_loop()
loop.run_until_complete()
