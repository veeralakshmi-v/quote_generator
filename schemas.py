from pydantic import BaseModel

class QuoteCreate(BaseModel):
    category: str

class QuoteResponse(BaseModel):
    id: int
    category: str
    text: str

    class Config:
        orm_mode = True
