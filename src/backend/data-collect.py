import asyncio
from logging import getLogger, INFO
from os import getenv

from dotenv import load_dotenv
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, JSONResponse

from db import RecordDeta, Count, VideoStatus


load_dotenv()
logger = getLogger(__name__)
logger.setLevel(INFO)

record = RecordDeta(youtube_api_key=getenv("YOUTUBE_TOKEN"))
app = APIRouter()


@app.get("/__space/v0/actions")
async def pong():
    return FileResponse("static/data-collector.html", media_type="text/html")


# handler
@app.post("/__space/v0/actions")
async def actions(request: Request):
    data = await request.json()
    event = data["event"]
    if event["id"] != "get-video-data":  # なんか不正されそう
        return JSONResponse({"message": "Who are you?"}, 401)

    all_videos = await record.get_videos(VideoStatus.ENABLED)
    asyncio.gather(
        []
    )
    data = Count()
    video = client.get_video_by_id(video_id="AjspnMNkGu8")
    if not video.items:
        return JSONResponse(
            {"message": "The video is not available"}
        )  # TODO: いい感じにする

    # db.put(
    #     {
    #         "date": now_date.isoformat(),
    #         "jst_date": now_date.astimezone(jst).isoformat(),
    #         "timestamp": round(now_date.timestamp()),
    #         "view_count": video.items[0].statistics.viewCount,  # type: ignore
    #     }
    # )
    logger.info("Added video info to database")


async def add_video_stastics(video_id: str):
    video = await asyncio.to_thread(record._yt_token.get_video_by_id, video_id=video_id)
    if not video.items:
        return
    count = video.items[0].statistics.viewCount
    await record.view_counter.add_video_data(Count(count=count, video_id=video_id))
    return True
