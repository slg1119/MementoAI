from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String(500), index=True)
    short_url = Column(String(500), index=True)
    hits = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
