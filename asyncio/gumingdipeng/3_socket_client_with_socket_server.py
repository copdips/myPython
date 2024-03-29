import socket

# 返回主动套接字
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    # 连接服务端
    client.connect(("localhost", 12345))
    while True:
        # 发送消息
        data = input("请输入内容: ")
        if data.strip().lower() in ("q", "quit", "exit"):
            print(f"data: {data}")
            # 在with context里面, 不再需要 client.close()
            print("Bye~~~")
            break
        client.send(data.encode("utf-8"))
        print(client.recv(1024).decode("utf-8"))
