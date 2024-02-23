from pydantic import BaseModel as _BaseModel


class YTVideoInput(_BaseModel):
    video_id: str
