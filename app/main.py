# ASGI door: wires the isolated completion feature without business logic.
from fastapi import FastAPI
from app.feature_completion.router import router

app = FastAPI(title='Multi-Provider LLM Routing Gateway — STEP-1')
app.include_router(router)

# Add privacy-safe persistent gateway outcome audit after route registration.
from app.core.request_audit_middleware import RequestAuditMiddleware
app.add_middleware(RequestAuditMiddleware)
