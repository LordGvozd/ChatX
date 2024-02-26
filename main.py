import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

import config
from src.pages import pages_router


app = FastAPI()

web_static_assets = StaticFiles(directory=config.TEMPLATES_DIR_PATH + "/assets/",
                                check_dir=True)
app.mount("/assets", web_static_assets, "Assets")
app.include_router(pages_router)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=8000, reload_includes=["*html", "*css", "*js"])
