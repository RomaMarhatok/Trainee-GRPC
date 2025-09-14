from .base import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Users(BaseModel):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False, index=True
    )
