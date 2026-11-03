from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, model_validator

class EventCreate(BaseModel):
    title: str = Field(min_length=3, max_length=255)
    start_time: datetime
    end_time: datetime
    location: str = Field(min_length=1, max_length=255)
    max_capacity: int = Field(gt=0)
    category_id: int
    organizer_id: int

    @model_validator(mode="after")
    def check_dates(self):
        if self.end_time <= self.start_time:
            raise ValueError("end_time must be after start_time")
        return self

class EventResponse(EventCreate):
    id: int
    status: str
    model_config = ConfigDict(from_attributes=True)