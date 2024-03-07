from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from database.database import get_db

router = APIRouter()


@router.get("/peaks/{peak_id}", response_model=schemas.Peak)
async def find_peak(peak_id: int, db: Session = Depends(get_db)):
    db_peak = crud.get_peak(db, peak_id)

    return db_peak
