import os
from threading import Thread
from time import sleep

threads = [Thread(target=lambda: sleep(60)) for i in range(10000)]

[t.start() for t in threads]
print(f"PID={os.getpid()}")

[t.join() for t in threads]
