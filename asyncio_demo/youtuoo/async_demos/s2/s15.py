from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Mount, Route


def homepage(request):
    return PlainTextResponse("Homepage")


async def about(request):
    username = request.path_params["username"]
    print(username)
    print(type(username))
    return PlainTextResponse("")


routes = [
    Route("/", endpoint=homepage),
    Mount(
        "/users",
        routes=[
            Route("/index", endpoint=homepage),
            Route("/about/me", endpoint=homepage),
            Route("/about/{username:int}", endpoint=about),
        ],
    ),
]

app = Starlette(routes=routes)
