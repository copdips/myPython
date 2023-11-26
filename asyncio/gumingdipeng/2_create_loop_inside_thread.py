# https://www.cnblogs.com/traditional/p/17363960.html
import asyncio
import threading

# 无论主线程还是子线程，毫无疑问都是可以创建事件循环的。只不过主线程既可以手动调用 new_event_loop 和 set_event_loop 来创建，也可以调用 get_event_loop（当循环不存在时内部自动创建）。
# ! 但对于子线程而言，只能采用第一种方式，也就是手动创建，如果直接调用 get_event_loop 是会报错的，至于原因，源码中写的很清楚了。


def create_loop():
    # 获取事件循环策略，如果没创建，那么就实例化 DefaultEventLoopPolicy 创建一个
    # 这个 DefaultEventLoopPolicy 也不是一个具体的类，而是根据操作系统会对应不同的类
    loop_policy = asyncio.get_event_loop_policy()
    # 通过策略的 new_event_loop 方法创建事件循环
    loop = loop_policy.new_event_loop()
    # 但以上两步可以直接合成一步，通过 asyncio.new_event_loop

    # 设置循环，将循环设置在策略的 _local 中，这样才能通过 get_event_loop 获取
    asyncio.set_event_loop(loop)
    loop.close()


threading.Thread(target=create_loop).start()
threading.Thread(target=create_loop).start()
threading.Thread(target=create_loop).start()
