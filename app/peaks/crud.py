from sqlalchemy.orm import Session
from . import models, schemas


def get_peak(db: Session, peak_id: int):
    return db.query(models.Peak).filter(models.Peak.id == peak_id).first()
