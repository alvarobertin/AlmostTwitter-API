# Python
# Pydantic

# FastAPI
from fastapi import FastAPI

# Models
from models import *

app = FastAPI()


@app.get(path="/")
def home():
    return {"API" : "Working"}