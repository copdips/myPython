import asyncio

import aioredis
import uvicorn
from fastapi import FastAPI

app = FastAPI()

# docker run -p 6379:6379 --name myredis -d redis
redis = aioredis.from_url("redis://127.0.0.1")


@app.get("/")
def index():
    """standard route"""
    return {"message": "Hello world"}


@app.get("/red")
async def red():
    """async route"""
    print("Coming request")
    await asyncio.sleep(3)
    await redis.hmset("car", {"key1": 1, "key2": 2})
    result = await redis.hgetall("car")
    # result = await redis.hget("car", "key1")
    print(result)
    return result


if __name__ == "__main__":
    uvicorn.run(
        "fastapi_demo:app", host="127.0.0.1", port=5000, log_level="info", reload=True
    )
