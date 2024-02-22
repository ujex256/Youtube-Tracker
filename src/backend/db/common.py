from pyyoutube import Api
from deta import Deta

from db.utils import is_video_exists
from db.view_count import _ViewCounter


class RecordDeta(Deta):
    def __init__(
        self,
        project_key: str | None = None,
        youtube_api_key: str | None = None,
        *,
        project_id: str | None = None
    ):
        super().__init__(project_key, project_id=project_id)  # type: ignore
        self.videos_db = self.Base("sugoi_videos")
        self.view_counter = _ViewCounter(self)
        self._yt_token = Api(api_key=youtube_api_key)

    def register_video(self, video_id, exist_ok=False):
        data = {"is_active": True, "channel_id": "", "dur": ""}
        status = is_video_exists(video_id, self._yt_token)
        if status.status is False:
            raise ValueError("The video is not found.")

        data["channel_id"] = status.response.items[0].snippet.channelId
        if exist_ok:
            self.videos_db.put(data, key=video_id)
        else:
            self.videos_db.insert(data, key=video_id)
