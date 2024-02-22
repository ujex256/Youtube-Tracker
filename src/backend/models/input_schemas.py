from pydantic import BaseModel


class YTVideoInput(BaseModel):
    video_id: str
