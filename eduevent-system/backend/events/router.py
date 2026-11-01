from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_db
from . import models, schemas

router = APIRouter()

@router.post("/", response_model=schemas.EventResponse,
             status_code=status.HTTP_201_CREATED)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    new_event = models.Event(**event.model_dump(), status="draft")
    db.add(new_event)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400,
                            detail="Invalid category_id or organizer_id")
    db.refresh(new_event)
    return new_event

@router.get("/ping")
def ping():
    return {"message": "Team gotowy!"}

@router.get("/{event_id}", response_model=schemas.EventResponse)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event