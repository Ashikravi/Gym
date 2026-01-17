from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers.log import router as log_router

app = FastAPI(title="AI Gym Coach")

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routers
app.include_router(log_router)
