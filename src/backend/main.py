from os import getenv

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from models import input_schemas
from data_collector import collector
from db import RecordDeta
from db.exceptions import VideoAlreadyRegistered, VideoNotFound


load_dotenv()
app = FastAPI()
app.include_router(collector)
record = RecordDeta(youtube_api_key=getenv("YOUTUBE_TOKEN"))


@app.get("/")
async def test():
    return "Hello, world!"


@app.post("/video/register")
async def register(a: input_schemas.YTVideoInput):
    try:
        await record.register_video(video_id=a.video_id)
    except VideoAlreadyRegistered as e:
        return JSONResponse(
            {"id": e.id, "msg": "The video has already registered."}, 400
        )
    except VideoNotFound as e:
        return JSONResponse(
            {"id": e.id, "msg": "The video is not found"}, 400
        )
    return JSONResponse({"status": True})
