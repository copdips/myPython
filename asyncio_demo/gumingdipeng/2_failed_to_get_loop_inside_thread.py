import asyncio
import threading


def create_loop():
    asyncio.get_event_loop()


threading.Thread(target=create_loop).start()
"""
RuntimeError: There is no current event loop in thread 'Thread-1'.
exception generated from : get_event_loop_policy().get_event_loop()
"""
