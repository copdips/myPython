import asyncio
import time


async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")
    loop.stop()


def blocking():
    # if this blocking sleep is larger thant 1 sec as defined in the main() asyncio.sleep, we will get an error.
    time.sleep(1.5)
    print(f"{time.ctime()} Hello from a thread!")


loop = asyncio.get_event_loop()

loop.create_task(main())
loop.run_in_executor(None, blocking)

loop.run_forever()

pending = asyncio.Task.all_tasks(loop=loop)
group = asyncio.gather(*pending)
loop.run_until_complete(group)
loop.close()

# Output:
# $ python quickstart_exe.py
# Sun Sep 17 14:17:38 2017 Hello!
# Sun Sep 17 14:17:38 2017 Hello from a thread!
# Sun Sep 17 14:17:39 2017 Goodby
