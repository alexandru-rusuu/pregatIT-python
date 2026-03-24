from pydantic import BaseModel
from typing import Optional

class TaskCreateRequest(BaseModel):
    title: str
    owner: str
    description: Optional[str] = ""

class TaskUpdateRequest(BaseModel):
    title: Optional[str] = None
    owner: Optional[str] = None
    description: Optional[str] = None

class TaskStatusChangeRequest(BaseModel):
    new_status: str

class TaskResponse(BaseModel):
    id: int
    title: str
    owner: str
    description: str
    status: str
    created_at: float
    updated_at: float