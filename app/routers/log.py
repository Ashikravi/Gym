from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse

from app.core.config import templates
from app.core.database import get_db
from app.schemas.log_schema import LogInput    
from sqlalchemy.orm import Session
from sqlalchemy import text

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/health/db")
def db_health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "DB connected ✅"}

@router.post("/log")
def log_data(data: LogInput):
    response = {"message": "Data logged", "received": data}

    if data.exercise:
        response["coach_feedback"] = "Good job training today 💪"

    if data.food:
        response["coach_feedback"] = "Nutrition logged. Stay consistent 🍗"

    if data.body_weight:
        response["coach_feedback"] = "Tracking progress is key 📈"

    return response
