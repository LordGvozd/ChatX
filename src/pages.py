from fastapi import FastAPI, APIRouter, Request
from fastapi.templating import Jinja2Templates

import config


pages_router = APIRouter()

templates = Jinja2Templates(directory=config.TEMPLATES_DIR_PATH)


@pages_router.get("/")
async def get_index_page(request: Request):
    return templates.TemplateResponse(request, name="index.html")


@pages_router.get("/chat")
async def get_index_page(request: Request):
    return templates.TemplateResponse(request, name="chat.html")
