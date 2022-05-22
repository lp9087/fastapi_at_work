from typing import Optional
from pydantic import BaseModel


class DateBaseInfo(BaseModel):
    id: int
    db_type: str
    db_name: str
    host: str
    port: int

    class Config:
        orm_mode = True


class DateBaseCreate(DateBaseInfo):
    pass


class DateBaseUpdate(BaseModel):
    db_type: Optional[str] = None
    db_name: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None

    class Config:
        orm_mode = True


class GetData(BaseModel):
    sql: str