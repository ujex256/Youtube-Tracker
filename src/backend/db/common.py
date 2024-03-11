from aiohttp.client_exceptions import ClientResponseError as _RespErr
from pyyoutube import Api
from deta import Deta
from pydantic import BaseModel

from db.utils import is_video_exists
from db.view_count import _ViewCounter
from db import exceptions as exp

from enum import Enum


class VideoStatus(Enum):
    ENABLED = {"enabled": True}
    DISABLED = {"enabled": False}


class YTVideo(BaseModel):
    video_id: str
    enabled: bool


class RecordDeta(Deta):
    def __init__(
        self,
        project_key: str | None = None,
        youtube_api_key: str | None = None,
        *,
        project_id: str | None = None
    ):
        super().__init__(project_key, project_id=project_id)  # type: ignore
        self.videos_db = self.AsyncBase("sugoi_videos")
        self.view_counter = _ViewCounter(self)
        self._yt_token = Api(api_key=youtube_api_key)

    async def register_video(self, video_id, exist_ok=False):
        data = {"enabled": True, "channel_id": "", "dur": ""}
        status = await is_video_exists(video_id, self._yt_token)
        if status.status is False:
            raise ValueError("The video is not found.")

        data["channel_id"] = status.response.items[0].snippet.channelId
        if exist_ok:
            await self.videos_db.put(data, key=video_id)
        else:
            try:
                await self.videos_db.insert(data, key=video_id)
            except _RespErr:
                raise exp.VideoAlreadyRegistered

    async def get_videos(self, status: VideoStatus | None = None):
        if status is None:
            return await self.videos_db.fetch()
        if not isinstance(status, VideoStatus):
            raise ValueError("status must be a VideoStatus")

        return await self.videos_db.fetch(status.value)

    async def get_video(self, video_id):
        found = await self.videos_db.fetch({"video_id": video_id})
        if found.count == 0:
            return None
        i = found.items[0]
        results = YTVideo(video_id=i["video_id"], status=i["enabled"])
        return results
