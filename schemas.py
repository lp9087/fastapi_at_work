from typing import List, Union, Optional

from pydantic import BaseModel


# class ItemBase(BaseModel):
#     title: str
#     description: Union[str, None] = None
#
#
# class ItemCreate(ItemBase):
#     pass
#
#
# class Item(ItemBase):
#     id: int
#     owner_id: int
#
#     class Config:
#         orm_mode = True
#
#
# class UserBase(BaseModel):
#     email: str
#
#
# class UserCreate(UserBase):
#     password: str
#
#
# class User(UserBase):
#     id: int
#     is_active: bool
#     items: List[Item] = []
#
#     class Config:
#         orm_mode = True


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