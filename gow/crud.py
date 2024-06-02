from sqlalchemy.orm import Session

from . import models, schemas


def create_record(db: Session, record: schemas.RecordCreate):
    db_record = models.Record(username=record.username, stage=record.stage, score=record.score)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Record).offset(skip).limit(limit).all()