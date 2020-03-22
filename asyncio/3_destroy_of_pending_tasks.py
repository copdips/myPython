# taskwarning.py
import asyncio


async def f(delay):
    await asyncio.sleep(delay)


loop = asyncio.get_event_loop()
t1 = loop.create_task(f(1))
t2 = loop.create_task(f(2))
loop.run_until_complete(t1)
loop.close()

# above code will throw error:
# Task was destroyed but it is pending!
# task: <Task pending name='Task-2' coro=<f() running at d:/xiang/git/myPython/asyncio/3_destroy_of_pending_tasks.py:6> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x000001A50F287CA0>()]>>
# This is because t2 is not finished when the loop is closed by the end of t1
