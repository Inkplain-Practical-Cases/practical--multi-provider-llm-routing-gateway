# ASGI door: wires the isolated completion feature without business logic.
from fastapi import FastAPI
from app.feature_completion.router import router

app = FastAPI(title='Multi-Provider LLM Routing Gateway — STEP-1')
app.include_router(router)
