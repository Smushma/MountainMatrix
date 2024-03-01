from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routers import peaks

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.include_router(peaks.router)


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
