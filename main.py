# Python
from typing import List
# Pydantic

# FastAPi
from fastapi import FastAPI

# routers
from controllers import router

app = FastAPI()

app.include_router(router)
