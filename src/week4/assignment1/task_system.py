import time
from custom_exceptions import TaskNotFoundError, InvalidStatusTransitionError
from db_handler import get_db_connection


class Task:
    def __init__(self, title: str, owner: str, description: str = "", status: str = "CREATED", created_at: float = None,
                 updated_at: float = None, task_id: int = None):
        self._id = task_id
        self._title = title
        self._owner = owner
        self._description = description
        self._status = status
        self._created_at = created_at or time.time()
        self._updated_at = updated_at or time.time()

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "title": self._title,
            "owner": self._owner,
            "description": self._description,
            "status": self._status,
            "created_at": self._created_at,
            "updated_at": self._updated_at
        }


class TaskManager:
    def __init__(self):
        self.valid_transitions = {
            "CREATED": ["IN_PROGRESS"],
            "IN_PROGRESS": ["IN_REVIEW", "DONE"],
            "IN_REVIEW": ["DONE", "IN_PROGRESS"],
            "DONE": []
        }

    def create_task(self, title: str, owner: str, description: str = "") -> Task:
        task = Task(title, owner, description)
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tasks (title, owner, description, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
                (task._title, task._owner, task._description, task._status, task._created_at, task._updated_at)
            )
            task._id = cursor.lastrowid
            conn.commit()
        return task

    def get_task_by_id(self, task_id: int) -> Task | None:
        with get_db_connection() as conn:
            row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
            if row:
                return Task(row['title'], row['owner'], row['description'], row['status'], row['created_at'],
                            row['updated_at'], row['id'])
            return None

    def update_task(self, task_id: int, title: str = None, owner: str = None, description: str = None):
        task = self.get_task_by_id(task_id)
        if not task:
            raise TaskNotFoundError(f"task {task_id} not found")

        new_title = title if title is not None else task._title
        new_owner = owner if owner is not None else task._owner
        new_desc = description if description is not None else task._description
        new_updated = time.time()

        with get_db_connection() as conn:
            conn.execute(
                "UPDATE tasks SET title = ?, owner = ?, description = ?, updated_at = ? WHERE id = ?",
                (new_title, new_owner, new_desc, new_updated, task_id)
            )
            conn.commit()

    def change_status(self, task_id: int, new_status: str):
        task = self.get_task_by_id(task_id)
        if not task:
            raise TaskNotFoundError(f"task {task_id} not found")

        if new_status not in self.valid_transitions.get(task._status, []):
            raise InvalidStatusTransitionError(f"invalid transition from {task._status} to {new_status}")

        with get_db_connection() as conn:
            conn.execute(
                "UPDATE tasks SET status = ?, updated_at = ? WHERE id = ?",
                (new_status, time.time(), task_id)
            )
            conn.commit()

    def list_tasks(self, status_filter: str = None, owner_filter: str = None, sort_field: str = "id"):
        query = "SELECT * FROM tasks WHERE 1=1"
        params = []

        if status_filter:
            query += " AND status = ?"
            params.append(status_filter)
        if owner_filter:
            query += " AND owner = ?"
            params.append(owner_filter)

        allowed_sort = ["id", "title", "owner", "status", "updated_at", "created_at"]
        if sort_field not in allowed_sort:
            sort_field = "id"

        query += f" ORDER BY {sort_field}"

        with get_db_connection() as conn:
            rows = conn.execute(query, params).fetchall()
            for row in rows:
                task = Task(row['title'], row['owner'], row['description'], row['status'], row['created_at'],
                            row['updated_at'], row['id'])
                print(task.to_dict())