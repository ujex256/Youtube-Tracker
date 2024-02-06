from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


# 仮でfastapi
@app.get("/")
async def kari():
    return HTMLResponse("<h1>Heallo World!</h1>This is frontend")
