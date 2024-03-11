from datetime import datetime as dt
from typing import Optional

from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
    field_serializer,
)

from db import common
from db.utils import jst_datetime, is_video_id
from db import exceptions as exp


class Count(BaseModel):
    count: int
    video_id: str
    date: dt = Field(default_factory=dt.utcnow)
    jst_date: dt = Field(default_factory=jst_datetime)
    timestamp: Optional[int]

    @field_validator("video_id")
    def _vid_validator(cls, v):
        if not is_video_id(v):
            raise ValueError("Invalid video id.")
        return v

    @model_validator(mode="after")
    def _timestamp_validator(self):
        if self.timestamp is not None:
            return self
        self.timestamp = self.date.timestamp()
        return self

    @field_serializer("date", "jst_date")
    def _serialize_isofmt(self, time: dt):
        return time.isoformat()


class _ViewCounter:
    def __init__(self, record: "common.RecordDeta") -> None:
        self.base_deta = record
        self.db = record.AsyncBase("view_count_db")

    async def add_video_data(self, data: Count):
        video = self.base_deta.get_video(data.video_id)
        if video is None:
            raise exp.VideoNotRegistered(
                f"The video \"{data.video_id}\" is not yet registered."
            )
        await self.db.put(data.model_dump_json())
