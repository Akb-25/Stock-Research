from sqlalchemy import Column,INTEGER,String
from fastapi import FastAPI,Request,Form
from fastapi.responses import RedirectResponse,HTMLResponse
from fastapi.templating import Jinja2Templates

app=FastAPI()
templates=Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/get-data",response_class=HTMLResponse)
async def get_data(request:Request,stock_name:str=Form(...)):
    return templates.TemplateResponse("form_result.html",{"request":request,"stock_name":stock_name})