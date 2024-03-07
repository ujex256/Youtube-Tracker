import re
from zoneinfo import ZoneInfo
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator, field_serializer

from db import common


class Count(BaseModel):
    count: int
    video_id: str
    date: Optional[datetime] = Field(default_factory=datetime.utcnow)
    jst_date: Optional[datetime] = Field(default=datetime.now(tz=ZoneInfo("Asia/Tokyo")))
    timestamp: Optional[int]

    @validator("video_id")
    def __post_init__(cls, v):
        if re.fullmatch(r"[a-zA-Z0-9_-]{11}", v) is None:
            raise ValueError("Invalid video id.")
        return v

    @field_serializer("date", "jst_date")
    def serialize_isofmt(self, time: datetime):
        return time.isoformat()


class _ViewCounter:
    def __init__(self, record: "common.RecordDeta") -> None:
        self.base_deta = record
        self.db = record.AsyncBase("view_count_db")

    async def add_video_data(self, data: Count):
        await self.db.put(data.model_dump_json())
