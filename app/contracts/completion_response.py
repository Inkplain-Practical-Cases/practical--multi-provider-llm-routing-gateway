# A stable public response independent of any future provider SDK.
from pydantic import BaseModel

class CompletionResponse(BaseModel):
    provider: str
    text: str
    trace_id: str
