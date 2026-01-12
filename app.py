from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="AI Gym Coach")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ------------------------
# Log workout
# ------------------------
@app.post("/log-workout")
def log_workout(
    exercise: str = Form(...),
    sets: int = Form(...),
    reps: int = Form(...),
    weight: float = Form(...)
):
    return {
        "message": "Workout logged successfully",
        "data": {
            "exercise": exercise,
            "sets": sets,
            "reps": reps,
            "weight": weight
        }
    }


# ------------------------
# Log food
# ------------------------
@app.post("/log-food")
def log_food(
    food: str = Form(...),
    quantity: float = Form(...)
):
    return {
        "message": "Food logged successfully",
        "data": {
            "food": food,
            "quantity": quantity
        }
    }


# ------------------------
# Body stats
# ------------------------
@app.post("/log-body")
def log_body(
    weight: float = Form(...),
    waist: float = Form(...)
):
    return {
        "message": "Body stats saved",
        "data": {
            "weight": weight,
            "waist": waist
        }
    }


# ------------------------
# AI Coach (placeholder)
# ------------------------
@app.get("/coach")
def ai_coach():
    return {
        "coach_message": "You are doing well. Increase protein intake today 💪"
    }
