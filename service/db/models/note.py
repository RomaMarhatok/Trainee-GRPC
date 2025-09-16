import uuid
from .base import BaseModel
from sqlalchemy import String, Text, UUID, ForeignKey
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
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.uuididf", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )

    def to_dict(self):
        return {
            "uuididf": str(self.uuididf),
            "user_uuididf": str(self.user_id),
            "name": self.name,
            "message": self.message,
        }
