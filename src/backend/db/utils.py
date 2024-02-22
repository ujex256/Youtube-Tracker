import re

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


def is_video_exists(id: str, api_client: Api) -> VideoStatus:
    vi = api_client.get_video_by_id(video_id=id)
    result = VideoStatus(status=True, response=vi)
    if vi.pageInfo.totalResults == 0:  # type: ignore
        result.status = False
    return result
