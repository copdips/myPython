# quickstart.py
import time
import asyncio


async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')
    loop.stop()


loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
pending = asyncio.Task.all_tasks(loop=loop)
group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()

# Output:
# $ python quickstart.py
# Sun Sep 17 14:17:37 2017 Hello!
# Sun Sep 17 14:17:38 2017 Goodbye!
