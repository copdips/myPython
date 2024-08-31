import asyncio


async def f(delay):
    await asyncio.sleep(1 / delay)
    return delay


loop = asyncio.get_event_loop()
for i in range(10):
    loop.create_task(f(i))

pending = asyncio.Task.all_tasks()
# if return_exceptions=False, the script will exit with exceptions:

# d:/xiang/git/myPython/asyncio/319_all_the_tasks_will_complete.py:13: DeprecationWarning: Task.all_tasks() is deprecated, use asyncio.all_tasks() instead
#   pending = asyncio.Task.all_tasks()
# Traceback (most recent call last):
#   File "d:/xiang/git/myPython/asyncio/319_all_the_tasks_will_complete.py", line 15, in <module>
#     results = loop.run_until_complete(group)
#   File "D:\xiang\tools\Scoop\apps\python\current\lib\asyncio\base_events.py", line 616, in run_until_complete
#     return future.result()
#   File "d:/xiang/git/myPython/asyncio/319_all_the_tasks_will_complete.py", line 5, in f
#     await asyncio.sleep(1 / delay)
# ZeroDivisionError: division by zero

# with return_exceptions=Turn, the script finished wihtout exceptions, so the loop won't
# stopped by error before all the   tasks are done.

# d:/xiang/git/myPython/asyncio/319_all_the_tasks_will_complete.py:13: DeprecationWarning: Task.all_tasks() is deprecated, use asyncio.all_tasks() instead
#   pending = asyncio.Task.all_tasks()
# Results: [8, 5, 2, 9, 6, 3, ZeroDivisionError('division by zero'), 7, 4, 1]
group = asyncio.gather(*pending, return_exceptions=True)
results = loop.run_until_complete(group)
print(f"Results: {results}")
loop.close()
