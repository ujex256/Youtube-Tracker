import os
import datetime

from deta import Deta
from dotenv import load_dotenv
from pyyoutube import Api


load_dotenv(override=False)
client = Api(api_key=os.getenv("YOUTUBE_TOKEN"), timeout=5)
deta = Deta(os.getenv("DETA_PROJECT_KEY", ""))


db = deta.Base("view_count_db")
now_date = datetime.datetime.now(tz=datetime.timezone.utc)
jst = datetime.timezone(datetime.timedelta(hours=9))
db.put(
    {
        "timestamp": round(now_date.timestamp()),
        "jst_timestamp": round(now_date.astimezone(jst).timestamp()),
        "view_count": client.get_video_by_id(video_id="AjspnMNkGu8").to_dict()["items"][0]["statistics"]["viewCount"]
    }
)
