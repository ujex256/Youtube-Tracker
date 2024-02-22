from pydantic import BaseModel


class YTVideo(BaseModel):
    video_id: str
    channel_id: str
