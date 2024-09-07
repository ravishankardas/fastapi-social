from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth,vote
from .config import settings

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse

# models.Base.metadata.create_all(bind=engine)

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

# Route to serve the home page (index.html)
@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/resume", response_class=HTMLResponse)
async def get_resume(request: Request):
    return templates.TemplateResponse("resume.html", {"request": request})



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)



# @app.get("/")
# def root():
#     return {"message": "Hello World, i have deployed this app on heroku"}
