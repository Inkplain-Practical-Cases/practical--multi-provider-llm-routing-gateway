# Validate the untrusted prompt and desired provider at the API boundary.
from typing import Literal
from pydantic import BaseModel, Field, field_validator

class CompletionRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=2000)
    preferred_provider: Literal['auto', 'openai', 'claude'] = 'auto'

    @field_validator('prompt')
    @classmethod
    def reject_blank_prompt(cls, value: str) -> str:
        if not value.strip():
            raise ValueError('prompt cannot be blank')
        return value.strip()
