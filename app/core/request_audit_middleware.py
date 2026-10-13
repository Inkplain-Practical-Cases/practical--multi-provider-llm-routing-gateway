"""Persist only route/status LLM gateway metadata; never prompts or completions."""
import asyncio
import time
from starlette.middleware.base import BaseHTTPMiddleware
from app.providers.provider_record_request_audit import provider_record_request_audit

class RequestAuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        begin=time.perf_counter()
        response=await call_next(request)
        path=getattr(request.scope.get("route"),"path",request.url.path)
        await asyncio.to_thread(provider_record_request_audit,request.method,path,response.status_code,(time.perf_counter()-begin)*1000)
        return response
