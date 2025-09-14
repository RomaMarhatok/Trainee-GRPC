from .base import BaseModel
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column


class Notes(BaseModel):
    __tablename__ = "notes"
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )
    message: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
