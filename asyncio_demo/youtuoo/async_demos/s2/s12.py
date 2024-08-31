from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse
from starlette.routing import Mount, Route, WebSocketRoute
from starlette.staticfiles import StaticFiles


def homepage(request: Request):
    return PlainTextResponse("Hello, world!")


def user_me(request: Request):
    username = "John Doe"
    return PlainTextResponse("Hello, %s!" % username)


def user(request: Request):
    username = request.path_params["username"]
    return PlainTextResponse("Hello, %s!" % username)


async def websocket_endpoint(websocket):
    await websocket.accept()
    await websocket.send_text("Hello, websocket!")
    await websocket.close()


def startup():
    print(1111)
    print("Ready to go")


async def startup2():
    print(222)
    print("Ready to go222")


def shutdown():
    print("The end")


routes = [
    Route("/", homepage),
    Route("/user/me", user_me),
    Route("/user/{username}", user),  # /user/me
    WebSocketRoute("/ws", websocket_endpoint),
    Mount("/static", StaticFiles(directory="static")),
]

app = Starlette(
    debug=True,
    routes=routes,
    on_startup=[startup, startup2],
    on_shutdown=[shutdown],
)


# app()
