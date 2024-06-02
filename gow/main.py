from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

VERSION = "0.0.2"

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"version": VERSION}


@app.post("/records/", response_model=schemas.Record)
async def create_record(record: schemas.RecordCreate, db: Session = Depends(get_db)):
    return crud.create_record(db=db, record=record)


@app.get("/records/", response_model=list[schemas.Record])
async def get_records(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_records(db, skip=skip, limit=limit)
