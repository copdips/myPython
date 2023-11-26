# https://www.cnblogs.com/traditional/p/17363960.html
import asyncio


async def delay(seconds):
    print(f"start sleep {seconds}")
    await asyncio.sleep(seconds)
    print("end sleep")
    return seconds


async def main():
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(asyncio.shield(delay_task), 1)
        print("return value:", result)
    except asyncio.TimeoutError:
        # shield() does not protect from timeout, so it throws TimeoutError
        print("timeout")
        # shield() does protect from being cancelled
        print("whether the task is cancelled:", delay_task.cancelled())
        # from where it throws TimeoutError, continue to run, and wait for it to finish
        result = await delay_task
        print("return value:", result)


asyncio.run(main())
