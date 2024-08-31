import asyncio

import aioredis


async def main():
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )

    async with redis.client() as conn:
        await conn.set("my_key", "my_value")
        val = await conn.get("my_key")
        print(val)


async def redis_pool():
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )
    await redis.set("kkkkkk", "1234567")
    val = await redis.get("kkkkkk")
    print(val)


# asyncio.run(main())
asyncio.run(redis_pool())
