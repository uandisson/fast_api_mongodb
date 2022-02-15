from fastapi import FastAPI

from crud import crud_router
from logger import config_log

app = FastAPI()
app.include_router(crud_router)

config_log()
