from sqlalchemy import Column, Integer, String, Text
from database import Base

class Quote(Base):
    __tablename__ = "quotes"
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(50))
    text = Column(Text)
