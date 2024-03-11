import re
import asyncio
from datetime import datetime
from zoneinfo import ZoneInfo

from pydantic import BaseModel, model_validator
from pyyoutube import Api, VideoListResponse


def extract_id(url: str):
    reg = r"(youtu.*be.*)\/(watch\?v=|embed\/|v|shorts|)(.*?((?=[&#?])|$))"
    mc = re.match(reg, url)
    if mc is not None:
        return mc.string


def is_video_id(id: str):
    return re.fullmatch(r"[a-zA-Z0-9_-]{11}", id) is not None


class VideoStatus(BaseModel):
    status: bool
    response: VideoListResponse | dict

    @model_validator(mode="after")
    def vall(self):
        if self.status is False:
            return self

        err_msg = "If the status is True, response.items must not be empty."
        if isinstance(self.response, dict):
            if not self.response["items"]:
                raise ValueError(err_msg)
        else:
            if not self.response.items:
                raise ValueError(err_msg)
        return self


async def is_video_exists(id: str, api_client: Api) -> VideoStatus:
    vi = await asyncio.to_thread(api_client.get_video_by_id, video_id=id)
    status = True
    if vi.pageInfo.totalResults == 0:  # type: ignore
        status = False
    result = VideoStatus(status=status, response=vi)
    return result


def jst_datetime():
    return datetime.now(tz=ZoneInfo("Asia/Tokyo"))
