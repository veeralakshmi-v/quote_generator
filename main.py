from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import Quote
from schemas import QuoteCreate, QuoteResponse
from ai_module import generate_quote

app = FastAPI(title="AI Quote Generator API")

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/generate", response_model=QuoteResponse)
async def generate_ai_quote(request: QuoteCreate, db: Session = Depends(get_db)):
    ai_text = await generate_quote(request.category)
    new_quote = Quote(category=request.category, text=ai_text)
    db.add(new_quote)
    db.commit()
    db.refresh(new_quote)
    return new_quote

@app.get("/quotes", response_model=list[QuoteResponse])
async def get_all_quotes(db: Session = Depends(get_db)):
    return db.query(Quote).all()
