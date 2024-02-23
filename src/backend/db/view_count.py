import re
from pydantic import BaseModel, validator

from db import common


class Count(BaseModel):
    count: int
    video_id: str

    @validator("video_id")
    def __post_init__(cls, v):
        if re.fullmatch(r"[a-zA-Z0-9_-]{11}", v) is None:
            raise ValueError("Invalid video id.")
        return v


class _ViewCounter:
    def __init__(self, record: "common.RecordDeta") -> None:
        self.base_deta = record
        self.db = record.AsyncBase("view_count_db")

    async def add_video_data(self, data: Count):
        await self.db.put(data.model_dump_json())
