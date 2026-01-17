from pydantic import BaseModel
from typing import Optional


class LogInput(BaseModel):
    exercise: Optional[str] = None
    sets: Optional[int] = None
    reps: Optional[int] = None
    weight: Optional[float] = None

    food: Optional[str] = None
    quantity: Optional[float] = None

    body_weight: Optional[float] = None
    waist: Optional[float] = None
