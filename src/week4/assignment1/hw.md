# Homework Proposal: SQLite "File Database" Integration (Task Management System)

## Prerequisite
This assignment is an **extension on top of** the previous weeks’ **Task Management System (JIRA-like)**:
- OOP `Task` + `TaskManager`
- workflow status transitions (`CREATED` → `IN_PROGRESS` → `IN_REVIEW` → `DONE`)
- CLI app (`app.py`)
- custom exceptions + tests (week3/assignment2)

In this assignment you will replace JSON persistence with a **SQLite file database**.

## Estimated Implementation Time
6-10 hours

## Core Concepts to Implement
*   **Working with Files and Data (SQLite):** Use Python's built-in `sqlite3` module to create a persistent, file-based relational database.
*   **Database Integration:** Refactor the task system to replace JSON I/O with SQL operations (CRUD).
*   **SQL Fundamentals (CRUD):** Implement methods for:
    *   **C**reate (INSERT)
    *   **R**ead (SELECT)
    *   **U**pdate (UPDATE)
    *   **D**elete (DELETE)
*   **OOP and Database Mapping:** Clean mapping between `Task` objects and database rows.
*   **Robust Error Handling:** Handle common database exceptions (`sqlite3.OperationalError`, `sqlite3.IntegrityError`) and reuse your custom exceptions where appropriate.

## Project Goal
Transition the Task Management System from object serialization (JSON) to a true “file database” using SQLite, improving data integrity and enabling reliable persistence and querying.

---

## Required Structure

1.  **`task_system.py` (Existing):** Contains `Task` and `TaskManager` classes.
2.  **`db_handler.py` (New File):** Dedicated module for:
    - connecting to SQLite
    - initializing schema
    - executing core DB operations
3.  **`app.py` (Existing):** Main CLI loop that now calls DB-driven methods through `TaskManager`.
4.  **(Recommended) `custom_exceptions.py` (Existing):** Continue using your custom exceptions.

---

## Database Schema Requirements

Create a database file named `tasks.db` with a table `tasks`:

- `id INTEGER PRIMARY KEY AUTOINCREMENT`
- `title TEXT NOT NULL`
- `description TEXT`
- `owner TEXT NOT NULL`
- `status TEXT NOT NULL`
- `created_at REAL NOT NULL`
- `updated_at REAL NOT NULL`

Notes:
- Store timestamps as `REAL` (e.g., `time.time()`).
- Status should be stored as text (e.g., `"CREATED"`).
- Enforce `NOT NULL` rules for critical fields.

---

## Functional Requirements (Tasks)

| Task | Module Concept Focus |
| :--- | :--- |
| **1. Database Handler Setup (`db_handler.py`)** | SQLite Connection and Schema |
| | **Description:** Implement a function `get_db_connection()` that connects to `tasks.db`. On first run, it must call `create_tables()` to create the `tasks` table (schema above). Use safe SQL and commit changes. |
| **2. Refactor Persistence: Remove JSON Save/Load** | Refactoring |
| | **Description:** Remove/stop using JSON file persistence. Replace `load_tasks()`/`save_tasks()` usage with DB reads/writes. You may keep the old JSON methods, but the application must use SQLite as the source of truth. |
| **3. TaskManager Refactor: Load Tasks from DB** | SQL SELECT and Object Mapping |
| | **Description:** Implement a DB-backed method such as `load_tasks_from_db()` (or refactor `load_tasks()` to use SQLite). It must: |
| | * connect via `db_handler.py` |
| | * run `SELECT ... FROM tasks` |
| | * construct `Task` objects from rows |
| | * handle `sqlite3.OperationalError` (database locked/corrupted) gracefully |
| **4. Task Creation: Insert into DB** | SQL INSERT, Auto-ID |
| | **Description:** Refactor `create_task(...)` so that creating a task also performs an `INSERT` into SQLite. The DB generates the ID automatically; then your code must read the inserted ID (`cursor.lastrowid`) and set it on the `Task` object. |
| **5. Task Update: Update Row in DB** | SQL UPDATE |
| | **Description:** Refactor `update_task(...)` to persist edits with an `UPDATE` statement. Update `updated_at` each time. If task ID doesn’t exist, raise `TaskNotFoundError` (or equivalent). |
| **6. Status Change: Workflow + DB Update** | Domain Rules + SQL UPDATE |
| | **Description:** Refactor `change_status(...)` so it: |
| | * validates transition using your existing workflow rules |
| | * updates `status` and `updated_at` in the database with `UPDATE` |
| | * raises `InvalidStatusTransitionError` for invalid transitions |
| **7. Listing/Filtering from DB** | SQL SELECT, Query Parameters |
| | **Description:** Update listing so it can query from DB (recommended) using optional filters: |
| | * filter by `owner` |
| | * filter by `status` |
| | * sorting (by `id`, `updated_at`, etc.) |
| | Use SQL parameters (`?`) to avoid SQL injection. |
| **8. Transaction and Connection Safety (`app.py`)** | Resource Management |
| | **Description:** Ensure connections/cursors are properly closed. Prefer `with sqlite3.connect(...) as conn:` or a helper that ensures `commit()` and `close()` are handled correctly. The CLI should not lose data if the app exits normally. |

---

## Suggested Implementation Steps

1.  Create `db_handler.py` with connection + schema creation.
2.  Implement DB CRUD functions (insert/select/update) and test them quickly with a small script.
3.  Refactor `TaskManager` methods (`create_task`, `update_task`, `change_status`, list/filter) to use SQLite.
4.  Update `app.py` to rely on DB-backed methods (no JSON save/load menu).
5.  Run your existing tests and update/add tests to cover DB behavior (optional but recommended).

---

## Deliverables
- `db_handler.py`
- Updated `task_system.py` using SQLite persistence
- Updated `app.py` using SQLite as storage (`tasks.db` created automatically)
- `tasks.db` should be created on first run and retain tasks between runs