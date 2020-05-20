from dataclasses import dataclass

from sqlalchemy import Column, DateTime, String, Integer, func
from extensions import db
from entities import translation


@dataclass
class Translation(db.Model):

    id: int
    added: str
    language: str
    original_text: str
    translated_text: str

    __tablename__ = 'translation'
    id = Column(Integer, primary_key=True)
    added = Column(DateTime, default=func.now())
    language = Column(String)
    original_text = Column(String)
    translated_text = Column(String)

    def get(self):
        return translation.Translation(self.language,
                                       self.original_text,
                                       self.translated_text)