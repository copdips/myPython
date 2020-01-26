def terminal():
    while True:
        msg = yield    # msg gets the value sent via a send() call
        if msg == 'exit':
            print("Bye!")
            break
        elif msg.startswith('echo'):
            print(msg.split('echo ', 1)[1])
        elif msg.startswith('eval'):
            print(eval(msg.split('eval', 1)[1]))

t = terminal()
next(t)
t.send("echo hello")
t.send("eval 1+1")
t.send("exit")