from importlib.metadata import version

from fastapi import FastAPI

from app.api.v1 import api_v1_router

app = FastAPI(title="Scribe API", version=version("scribe-server"))
app.include_router(api_v1_router)
