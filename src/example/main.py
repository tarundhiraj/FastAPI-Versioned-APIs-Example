from fastapi import FastAPI
from sub_app import sub_app

app = FastAPI()

app.mount("/subapp", sub_app)