from fastapi import FastAPI, APIRouter, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException

import config
from src.chat.chat import *
from src.data.repository import InMemoryRepo

pages_router = APIRouter()

repo = InMemoryRepo()
chat = Chat(id=1,
            messages=[],
            members=[User(
                id=1,
                name="User"
            )])

templates = Jinja2Templates(directory=config.TEMPLATES_DIR_PATH)


@pages_router.get("/")
async def get_index_page(request: Request):
    return templates.TemplateResponse(request, name="index.html")


@pages_router.get("/get_all_messages")
async def get_all_messages(request: Request):
    return chat.messages


@pages_router.post("/add_message")
async def get_all_messages(message: Message, request: Request, response: Response):
    try:
        chat.add_message(message)
    except UserNotInChatError:
        response.status_code = 403
        return HTTPException(status_code=403, detail="User not in chat")
    return 200
