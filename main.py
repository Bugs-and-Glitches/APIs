from fastapi import FastAPI , Request
from routes.routes import router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from static import *
from pathlib import Path
import os

BASE_DIR = Path("Apis/templates").resolve().parent

# templates = Jinja2Templates(directory=os.path.abspath(os.path.expanduser('templates')))

app = FastAPI()
app.include_router(router)
app.mount('/static', StaticFiles(directory='static'),  name='static')

@app.get("/" , response_class=HTMLResponse)
async def get(request: Request):
    return HTMLResponse('''
    
    <h1> APIs From Bugs and Glitches Devloper Comunity </h1>
'''

    )