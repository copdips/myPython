import asyncio

from starlette.applications import Starlette
from starlette.background import BackgroundTask
from starlette.responses import JSONResponse
from starlette.routing import Route


async def signup(request):
    data = await request.json()
    username, email = data["username"], data["email"]
    task = BackgroundTask(send_welcome_email, to_address=email)
    message = {"status": "Signup successful"}
    return JSONResponse(message, background=task)


async def send_welcome_email(to_address):
    await asyncio.sleep(5)
    print("模拟发邮件")


routes = [Route("/user/signup", endpoint=signup, methods=["POST"])]

app = Starlette(routes=routes)
