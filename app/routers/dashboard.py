from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.core.template_config import templates

router = APIRouter(tags=["dashboard"])

#TODO serve page
@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})