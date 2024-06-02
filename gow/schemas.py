from typing import Union
from pydantic import BaseModel


class RecordBase(BaseModel):
    stage: str


class RecordCreate(RecordBase):
    username: str
    score: str


class Record(RecordCreate):
    id: int

    class Config:
        orm_mode = True