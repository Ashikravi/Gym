from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional


app = FastAPI(title="AI Gym Coach")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



# ------------------------
# Data schema
# ------------------------
class LogInput(BaseModel):
    exercise: Optional[str] = None
    sets: Optional[int] = None
    reps: Optional[int] = None
    weight: Optional[float] = None

    food: Optional[str] = None
    quantity: Optional[float] = None

    body_weight: Optional[float] = None
    waist: Optional[float] = None


# ------------------------
# Single  endpoint
# ------------------------
@app.post("/log")
def log_data(data: LogInput):
    response = {"message": "Data logged", "received": data}

    if data.exercise:
        response["coach_feedback"] = "Good job training today 💪"

    if data.food:
        response["coach_feedback"] = "Nutrition logged. Stay consistent 🍗"

    if data.body_weight:
        response["coach_feedback"] = "Tracking progress is key 📈"

    return response
