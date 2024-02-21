from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/")
async def chat():
    return HTMLResponse("""
ChatX
    """)
