# SuperFastPython.com
# get the http status of a webpage
import asyncio


# main coroutine
async def main():
    # define the url details
    host, port, path = "www.google.com", 443, "/"
    # open the connection
    reader, writer = await asyncio.open_connection(host, port, ssl=True)
    # send GET request
    query = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    # encode the query as bytes and send to server
    writer.write(query.encode())
    # wait for the bytes to be written to the socket
    await writer.drain()
    # read the single line response
    response = await reader.readline()
    # decode the bytes into a string and strip white space
    status = response.decode().strip()
    # report the status
    print(status)
    # close the socket connection
    writer.close()


# run the asyncio program
asyncio.run(main())
