from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request: Request):
    data = await request.form()
    print(data.get("name"))
    return JSONResponse({})


routes = [
    Route("/", homepage, methods=["POST"]),
]

app = Starlette(debug=True, routes=routes)
