from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base


class Snippet(Base):
    __tablename__ = "snippets"

    id = Column(String, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    language = Column(String, nullable=False)
    tags = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())