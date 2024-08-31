import socket

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
server.bind(("localhost", 12345))
# 调用 setblocking 方法，传入 False
# 表示将监听套接字和已连接套接字的类型设置为非阻塞
server.setblocking(False)
server.listen(5)

while True:
    try:
        # 非阻塞的监听套接字调用 accept() 时
        # 如果发现没有客户端连接，则会立刻抛出 BlockingIOError
        # 因此这里写了个死循环
        conn, addr = server.accept()
        conn.setblocking(False)
    except BlockingIOError:
        print("没有客户端连接")
        pass
    else:
        break

while True:
    try:
        # 同理，非阻塞的已连接套接字在调用 recv() 时
        # 如果发现客户端没有发数据，那么同样会报错
        msg = conn.recv(1024)
    except BlockingIOError:
        print("客户端没有发数据")
        pass
    else:
        print(msg.decode("utf-8"))
        conn.send(b"data from server")
