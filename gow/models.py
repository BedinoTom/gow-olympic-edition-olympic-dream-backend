from sqlalchemy import Column, Integer, String

from gow.database import Base

class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    stage = Column(String(255))
    score = Column(String(255))