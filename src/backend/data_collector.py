import asyncio
from logging import INFO, getLogger
from os import getenv

from dotenv import load_dotenv
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, JSONResponse

from db import Count, RecordDeta, VideoStatus


load_dotenv()
logger = getLogger(__name__)
logger.setLevel(INFO)

record = RecordDeta(youtube_api_key=getenv("YOUTUBE_TOKEN"))
collector = APIRouter()


@collector.get("/__space/v0/actions")
async def pong():
    return FileResponse("static/data-collector.html", media_type="text/html")


# handler
@collector.post("/__space/v0/actions")
async def actions(request: Request):
    data = await request.json()
    event = data["event"]
    if event["id"] != "getting":  # なんか不正されそう
        return JSONResponse({"message": "Who are you?"}, 401)

    all_videos = await record.get_videos(VideoStatus.ENABLED)
    semaphore = asyncio.Semaphore(5)

    tasks = [add_video_statistics(i["key"], semaphore) for i in all_videos.items]
    await asyncio.gather(*tasks)
    logger.info("Added video info to database")


async def add_video_statistics(video_id: str, sem: asyncio.Semaphore):
    async with sem:
        video = await asyncio.to_thread(record._yt_token.get_video_by_id, video_id=video_id)
    if not video.items:
        return
    count = video.items[0].statistics.viewCount
    await record.view_counter.add_video_data(Count(count=count, video_id=video_id))
    return True
