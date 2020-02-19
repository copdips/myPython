def download_webpage(url):
    print(url)

def update_stats(url):
    print(url)

def process(data):
    print(data)

# The blocking way
from contextlib import contextmanager


@contextmanager
def web_page(url):
    data = download_webpage(url)
    yield data
    update_stats(url)

with web_page('google.com') as data:
    process(data)


# The non­blocking way on web_page(), but inside with some blocking calls.
from contextlib import asynccontextmanager


@asynccontextmanager
async def web_page(url):
    data = await download_webpage(url)
    yield data
    await update_stats(url)

async with web_page('google.com') as data:
    process(data)


# The non­-blocking way on web_page(), and also inside with some non-blocking calls.
from contextlib import asynccontextmanager


@asynccontextmanager
async def web_page(url):
    loop = asyncio.get_event_loop()
    # * loop.run_in_executor() converts a blocking call to a non-blocking call
    # * by running the call in a separate thread
    data = await loop.run_in_executor(None, download_webpage, url)
    yield data
    await loop.run_in_executor(None, update_stats, url)

async with web_page('google.com') as data:
    process(data)