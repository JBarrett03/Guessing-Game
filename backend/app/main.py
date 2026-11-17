from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from sqlalchemy import select, text

from .database import get_db
from .models import Character
from .schemas import CharacterRead

app = FastAPI(title="Guessing Game API")

# Allow React to communicate with Python

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Test database connection
@app.get("/api/health/db")
def database_health(db: Session = Depends(get_db)):

    db.execute(text("SELECT 1"))

    return { "database": "connected" }

# Retrieve all characters
@app.get("/api/characters", response_model = list[CharacterRead])
def get_all_characters(limit: int = Query(100, ge=1, le=500), offset: int = Query(0, ge=0), db: Session = Depends(get_db)):

    statement = (
        select(Character)
        .order_by(Character.id)
        .limit(limit)
        .offset(offset)
    )

    characters = db.scalars(statement).all()

    return characters

# Retrieve a single character
@app.get("/api/characters/{character_id}", response_model = CharacterRead)
def get_character(character_id: int, db: Session = Depends(get_db)):

    character = db.get(Character, character_id)

    if character is None:
        raise HTTPException(status_code = 404, detail = "Character not found")

    return character