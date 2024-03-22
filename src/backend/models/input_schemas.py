from pydantic import BaseModel as _BaseModel
from pydantic import field_validator, Field

from db.utils import is_video_id


class YTVideoInput(_BaseModel):
    video_id: str

    @field_validator("video_id")
    def _id_validator(cls, v):
        if not is_video_id(v):
            raise ValueError
        return v
