# better than asyncio in terms of event loop, nearly as fast as golang.
# django v3 and fastapi both use uvicorn as asgi, which is based on uvloop as event loop.

# pip install uvloop


import asyncio

import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
