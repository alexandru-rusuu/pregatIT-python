from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from schemas import TaskCreateRequest, TaskUpdateRequest, TaskStatusChangeRequest, TaskResponse
from task_system import TaskManager
from custom_exceptions import TaskNotFoundError, InvalidStatusTransitionError
from db_handler import create_tables

create_tables()

app = FastAPI(title="Task Management API")
manager = TaskManager()

@app.exception_handler(TaskNotFoundError)
async def not_found_handler(request: Request, exc: TaskNotFoundError):
    return JSONResponse(status_code=404, content={"detail": str(exc)})

@app.exception_handler(InvalidStatusTransitionError)
async def transition_error_handler(request: Request, exc: InvalidStatusTransitionError):
    return JSONResponse(status_code=409, content={"detail": str(exc)})

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(status_code=422, content={"detail": str(exc)})

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(req: TaskCreateRequest):
    if not req.title.strip() or not req.owner.strip():
        raise ValueError("Title and owner cannot be empty")
    task = manager.create_task(req.title, req.owner, req.description)
    return task.to_dict()

@app.get("/tasks", response_model=list[TaskResponse])
def list_tasks(status: str = None, owner: str = None, sort_by: str = "id"):
    tasks = manager.list_tasks(status, owner, sort_by)
    return [t.to_dict() for t in tasks]

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    task = manager.get_task_by_id(task_id)
    if not task:
        raise TaskNotFoundError(f"task {task_id} not found")
    return task.to_dict()

@app.patch("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, req: TaskUpdateRequest):
    if req.title is None and req.owner is None and req.description is None:
        raise ValueError("no fields to update")
    manager.update_task(task_id, req.title, req.owner, req.description)
    return manager.get_task_by_id(task_id).to_dict()

@app.post("/tasks/{task_id}/status", response_model=TaskResponse)
def change_status(task_id: int, req: TaskStatusChangeRequest):
    manager.change_status(task_id, req.new_status)
    return manager.get_task_by_id(task_id).to_dict()