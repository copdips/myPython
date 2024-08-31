from starlette.responses import FileResponse


async def app(scope, receive, send):
    assert scope["type"] == "http"
    response = FileResponse("s14.py")
    await response(scope, receive, send)
