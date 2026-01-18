from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from app.core.auth_config import supabase
from app.core.template_config import templates
from app.schemas.auth_schema import SigninSchema, SignupSchema

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/signup", response_class=HTMLResponse)
def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@router.post("/signup")
def signup(data: SignupSchema):
    try:
        res = supabase.auth.sign_up({
            "email": data.email,
            "password": data.password,
            "options": {
                "email_redirect_to": "http://localhost:8000/welcome"
            }
        })

        return {"message": "Signup success ✅ Check email for confirmation", "user": res.user}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/signin", response_class=HTMLResponse)
def signin_page(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})

@router.post("/signin")
def signin(data: SigninSchema):
    try:
        res = supabase.auth.sign_in_with_password({
            "email": data.email,
            "password": data.password,
        })

        return {"message": "Login success ✅"}
    
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid email or password ❌")
