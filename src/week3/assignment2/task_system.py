import json
import time
from datetime import datetime
from custom_exceptions import InvalidInputError, TaskNotFoundError, InvalidStatusTransitionError, EmptyUndoStackError


class Task:
    def __init__(self, title: str, owner: str, description: str = "", task_id: int = None, status: str = "CREATED",
                 created_at: str = None, updated_at: str = None):
        self._id: int = task_id if task_id else int(time.time() * 1000)
        self._title: str = title
        self._owner: str = owner
        self._description: str = description
        self._status: str = status
        now: str = datetime.now().isoformat()
        self._created_at: str = created_at if created_at else now
        self._updated_at: str = updated_at if updated_at else now

    def to_dict(self) -> dict:
        return {
            "_id": self._id,
            "_title": self._title,
            "_owner": self._owner,
            "_description": self._description,
            "_status": self._status,
            "_created_at": self._created_at,
            "_updated_at": self._updated_at
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title=data["_title"],
            owner=data["_owner"],
            description=data["_description"],
            task_id=data["_id"],
            status=data["_status"],
            created_at=data["_created_at"],
            updated_at=data["_updated_at"]
        )

    def __str__(self) -> str:
        return f"[{self._id}] {self._title} ({self._status}) - {self._owner}"


class TaskManager:
    def __init__(self, filename: str = "tasks.json"):
        self.tasks: list[Task] = []
        self.undo_stack: list[list[dict]] = []
        self.filename: str = filename
        self.workflow_rules: dict[str, list[str]] = {
            "CREATED": ["IN_PROGRESS", "DONE"],
            "IN_PROGRESS": ["DONE", "BLOCKED"],
            "BLOCKED": ["IN_PROGRESS", "DONE"],
            "DONE": []
        }

    def _save_state(self):
        self.undo_stack.append([t.to_dict() for t in self.tasks])

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                data: list[dict] = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    def create_task(self, title: str, owner: str, description: str = "") -> Task:
        if not title or not title.strip():
            raise InvalidInputError("title cannot be empty.")
        if not owner or not owner.strip():
            raise InvalidInputError("owner cannot be empty.")

        self._save_state()
        new_task: Task = Task(title, owner, description)
        self.tasks.append(new_task)
        return new_task

    def list_tasks(self, filter_status: str = None, filter_owner: str = None, sort_by: str = "id") -> list[Task]:
        filtered: list[Task] = [
            t for t in self.tasks
            if (not filter_status or t._status == filter_status) and
               (not filter_owner or t._owner == filter_owner)
        ]
        sort_key: str = sort_by if sort_by.startswith("_") else f"_{sort_by}"
        return sorted(filtered, key=lambda t: getattr(t, sort_key, getattr(t, "_id")))

    def get_task_by_id(self, task_id: int) -> Task:
        for t in self.tasks:
            if t._id == task_id:
                return t
        raise TaskNotFoundError(f"task ID {task_id} not found.")

    def update_task(self, task_id: int, title: str = None, owner: str = None, description: str = None):
        task: Task = self.get_task_by_id(task_id)

        if title is not None and not title.strip():
            raise InvalidInputError("title cannot be updated to empty.")
        if owner is not None and not owner.strip():
            raise InvalidInputError("owner cannot be updated to empty.")

        self._save_state()
        if title: task._title = title
        if owner: task._owner = owner
        if description is not None: task._description = description
        task._updated_at = datetime.now().isoformat()

    def change_status(self, task_id: int, new_status: str):
        task: Task = self.get_task_by_id(task_id)
        if new_status in self.workflow_rules.get(task._status, []):
            self._save_state()
            task._status = new_status
            task._updated_at = datetime.now().isoformat()
        else:
            raise InvalidStatusTransitionError(f"transition from {task._status} to {new_status} is not allowed.")

    def undo_last_action(self):
        if self.undo_stack:
            previous_state: list[dict] = self.undo_stack.pop()
            self.tasks = [Task.from_dict(d) for d in previous_state]
        else:
            raise EmptyUndoStackError("nothing to undo.")