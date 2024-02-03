# from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/item/{id}", response_class=HTMLResponse)
def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        "./item.html",
        {
            "request": request,
            "id": id,
        },
    )


# app = FastAPI()
# - 객체지향 싱글톤 패턴
# @app.get("/")
# - 라우터
# - @app.ge 데코레이터
