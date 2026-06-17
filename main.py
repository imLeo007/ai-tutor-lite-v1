from fastapi import FastAPI, Request

from fastapi.templating import Jinja2Templates

from fastapi.staticfiles import StaticFiles

from fastapi.responses import HTMLResponse

from routers.auth import router as auth_router
from routers.chat import router as chat_router

app = FastAPI()

# templates directory

templates = Jinja2Templates(directory="templates")

# static files directory

app.mount("/static", StaticFiles(directory="static"), name="static")

# including routers

app.include_router(auth_router)
app.include_router(chat_router)


# rendering templates

# login page rendering
@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )

# signup page rendering
@app.get("/signup-page", response_class=HTMLResponse)
async def signup_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="signup.html"
    )

# chat page rendering
@app.get("/chat-page", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="chat.html"
    )