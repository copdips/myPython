from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.responses import PlainTextResponse
from starlette.routing import Route


class Homepage(HTTPEndpoint):
    async def get(self, request):
        return PlainTextResponse(request.base_url)


class User(HTTPEndpoint):
    async def get(self, request):
        username = request.path_params["username"]
        return PlainTextResponse(f"GET: {username}")

    async def post(self, request):
        username = request.path_params["username"]
        return PlainTextResponse(f"POST: {username}")


routes = [Route("/", endpoint=Homepage), Route("/{username}", User)]

app = Starlette(routes=routes)
