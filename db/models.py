from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Headline(Base):
    __tablename__ = 'headline'
    id = Column(Integer, primary_key=True)
    added = Column(DateTime, default=func.now())
    language = Column(String)
    original_text = Column(String)
    translated_text = Column(String)
