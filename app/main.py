from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from app.routers.auth import router as auth_router
from app.routers.dashboard import router as dashboard

app = FastAPI(title="AI Gym Coach")

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routers
app.include_router(auth_router)
app.include_router(dashboard)

@app.get("/")
def root():
    return RedirectResponse(url="/auth/signin", status_code=302)