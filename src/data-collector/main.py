import datetime
import os
from logging import getLogger, INFO

from deta import Deta
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from pyyoutube import Api

load_dotenv(override=True)
logger = getLogger(__name__)
logger.setLevel(INFO)
client = Api(api_key=os.getenv("YOUTUBE_TOKEN", ""), timeout=5)
deta = Deta()  # project_keyは環境変数から取得される
app = FastAPI()


@app.get("/")
async def pong():
    return FileResponse("index.html", media_type="text/html")


# handler
@app.post("/__space/v0/actions")
async def actions(request: Request):
    data = await request.json()
    event = data["event"]
    if event["id"] != "get-video-data":  # なんか不正されそう
        return JSONResponse({"message": "Who are you?"}, 401)

    db = deta.Base("view_count_db")
    now_date = datetime.datetime.now(tz=datetime.timezone.utc)
    jst = datetime.timezone(datetime.timedelta(hours=9))

    video = client.get_video_by_id(video_id="AjspnMNkGu8")
    if not video.items:
        return JSONResponse(
            {"message": "The video is not available"}
        )  # TODO: いい感じにする

    db.put(
        {
            "date": now_date.isoformat(),
            "jst_date": now_date.astimezone(jst).isoformat(),
            "timestamp": round(now_date.timestamp()),
            "view_count": video.items[0].statistics.viewCount,  # type: ignore
        }
    )
    logger.info("Added video info to database")
