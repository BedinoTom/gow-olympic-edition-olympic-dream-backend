from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

VERSION = "0.0.5"

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


@app.delete("/records/{record_id}")
async def delete_record(record_id: int, db: Session = Depends(get_db)):
    try:
        crud.delete_record(db, record_id=record_id)
    except Exception:
        return {
            "status": "failed"
        }
    return {
        "status": "ok"
    }