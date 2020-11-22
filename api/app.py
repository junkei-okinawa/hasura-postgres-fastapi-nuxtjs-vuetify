from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
# app.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env  # Jinja2.Environment : filterやglobalの設定用

@app.get('/admin')
def admin(request: Request):
    return templates.TemplateResponse('admin.html',
                                      {'request': request,
                                      'username': 'admin'})

@app.get("/")
def read_root():
  return {"Hello": "test"}

@app.get("/index")
def index(request: Request):
  return templates.TemplateResponse('index.html', {'request': request})


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("react-test.html", {"request": request, "id": id})
