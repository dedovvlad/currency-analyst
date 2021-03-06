from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from src.utils.database import Base


class TelegramGroups(Base):
    __tablename__ = "telegram_groups"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    id_chat = Column(String, unique=True, index=True)
    title = Column(String, unique=False, index=True)
    type = Column(String, unique=False, index=True)
