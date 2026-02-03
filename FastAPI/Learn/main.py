from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory = "templates")

todos = ["Learn FastAPI", "Build a UI", "Deploy App"]

@app.get("/", response_class = HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@app.post("/add")
async def add_todo(request: Request, todo: str = Form(...)):
    todos.append(todo)
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})