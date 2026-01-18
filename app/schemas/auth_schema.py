from pydantic import BaseModel, EmailStr
from typing import Optional

class SignupSchema(BaseModel):
    email: EmailStr
    password: str

class SigninSchema(BaseModel):
    email: EmailStr
    password: str