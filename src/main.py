from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .database import crud, models, schemas
from .database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root(db: Session = Depends(get_db)):
    return {"message": "Hello World"}
