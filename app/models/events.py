from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.utils.init_db import Base

from datetime import datetime


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    event_title = Column(String, index=True, nullable=False)
    event_type = Column(String, index=True, nullable=False)
    event_date = Column(String, nullable=False)
    event_time = Column(String, index=True, nullable=False)
    event_location = Column(String, nullable=False)
    event_address = Column(String, nullable=False)
    age_range = Column(String, nullable=False)
    is_free_event = Column(Boolean, nullable=False)
    event_cost = Column(String, nullable=True)
    other = Column(String, nullable=False) 
    created_at = Column(DateTime(), default=datetime.now(), nullable=False, index=True)
    
