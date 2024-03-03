import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

import config
from src.data.repository import InMemoryRepo
from src.pages import pages_router
from src.web.web_chat import WebChat


app = FastAPI()

web_static_assets = StaticFiles(directory=config.TEMPLATES_DIR_PATH + "/assets/",
                                check_dir=True)
app.mount("/assets", web_static_assets, "Assets")
app.include_router(pages_router)

web_chat_router = APIRouter(prefix="/chat")
web_chat = WebChat(
    router=web_chat_router,
    repo=InMemoryRepo()
)
web_chat.create_chat_endpoints()

app.include_router(web_chat_router)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=8000, reload_includes=["*html", "*css", "*js"])
