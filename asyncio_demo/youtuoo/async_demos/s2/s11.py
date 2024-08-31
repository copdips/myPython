from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request: Request):
    print(request.headers)
    return JSONResponse({"hello": "world"})


async def websocket_endpoint(websocket):
    await websocket.accept()
    await websocket.send_text("Hello, websocket!")
    await websocket.close()


app = Starlette(
    debug=True, routes=[Route("/", homepage), WebSocketRoute("/ws", websocket_endpoint)]
)
