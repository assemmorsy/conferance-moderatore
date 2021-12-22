from typing import Optional
from pydantic import BaseModel
import datetime


class DoctorBase(BaseModel):
    name: str
    file_path: Optional[str] = None
    talk_id: int


class DoctorCreate(DoctorBase):
    pass


class Doctor(DoctorBase):
    id: int

    class Config:
        orm_mode = True


class TalkBase(BaseModel):
    name: str
    start_time: datetime
    session_id: int


class TalkCreate(TalkBase):
    pass


class Talk(TalkBase):
    id: int
    doctors: list[Doctor] = []

    class Config:
        orm_mode = True


class SessionBase(BaseModel):
    name: str
    date: datetime.date


class SessionCreate(SessionBase):
    pass


class Session(SessionBase):
    id: int
    talks: list[Talk] = []

    class Config:
        orm_mode = True


"""
class Hall(BaseModel):
    name: str
    from_date: datetime
    to_date: datetime
    sessions: list[Session]


class Conf(BaseModel):
    name: str
    halls: Optional[list[Hall]] = None
"""
