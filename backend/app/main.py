from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from .database import get_db

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Python backend is running!"
    }

@app.get("/api/health/db")
def database_health(db: Session = Depends(get_db)):
    
    db.execute(text("SELECT 1"))

    return {
        "database": "connected"
    }