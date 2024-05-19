from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    content: str
    is_spam: Optional[bool] = False
    is_ad: Optional[bool] = False


class PostCreate(PostBase):
    pass


class Post(PostBase):
    post_id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class ReportBase(BaseModel):
    reason: str
    status: Optional[str] = "pending"


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    report_id: int
    post_id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
