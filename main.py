# Python
from typing import List
# Pydantic

# FastAPi
from fastapi import FastAPI

# routers
from controllers import router

# database
from config.database import Session, engine, Base

app = FastAPI()
app.title = "AlmostTwitterAPI"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)

app.include_router(router)
