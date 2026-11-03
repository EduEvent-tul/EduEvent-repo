from sqlalchemy import Column, BigInteger, Integer, String, DateTime
from database import Base

class EventCategory(Base):
    __tablename__ = "event_categories"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

class Event(Base):
    __tablename__ = "events"

    id = Column(BigInteger, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    location = Column(String(255), nullable=False)
    max_capacity = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False, default="draft")
    category_id = Column(BigInteger, nullable=False)
    organizer_id = Column(BigInteger, nullable=False)