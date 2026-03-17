# Homework Proposal: Migrate the Task Management App from CLI to REST API (FastAPI)

## Prerequisite
This assignment is an **extension on top of** the existing Task Management System from previous weeks:

- `Task` + `TaskManager` (OOP)
- workflow/lifecycle status transitions (`CREATED` → `IN_PROGRESS` → `IN_REVIEW` → `DONE`)
- SQLite persistence (`tasks.db`)
- custom exceptions and unit tests (recommended to keep)

In this assignment, you will **remove the CLI** and expose the same functionality through **RESTful endpoints** using **FastAPI**.

## Estimated Implementation Time
8-14 hours

## Core Concepts to Implement
- **REST API design:** resources, HTTP methods, status codes, path/query parameters
- **FastAPI framework basics:** routes, request/response models, validation
- **Pydantic models:** input schemas vs output schemas
- **Exception mapping:** convert domain exceptions into proper HTTP errors (`HTTPException`)
- **SQLite integration:** reuse your existing DB layer
- **Testing APIs (recommended):** `fastapi.testclient.TestClient` for endpoint tests
- **OpenAPI docs:** ensure endpoints show correctly in `/docs`

---

## Project Goal
Convert your local CLI-based app into a web API that can be used by any client (browser, Postman, frontend app) while keeping:

- the **same domain rules** (workflow transitions, validation)
- the **same persistence** (SQLite file database)
- a clear separation between **API layer** and **business logic**

---

## Target API Functionality (What the REST API must support)

Minimum endpoints:

1. Create a task
2. List tasks (with filtering by status and/or owner)
3. Get task by ID (details)
4. Update task fields (title/description/owner)
5. Change task status (enforce lifecycle transitions)

Optional endpoints (bonus):

- Delete task
- List available statuses + allowed transitions (helper endpoint)
- Health check endpoint (`GET /health`)

---

## Required Structure (Suggested)

You may adapt naming, but keep the layers separated:

1. `task_system.py` (existing)
   - `Task`, `TaskManager`, workflow rules, DB calls (or calls into db handler/repo)

2. `db_handler.py` (existing)
   - `get_db_connection()`, schema creation, DB utilities

3. `api.py` (new)
   - FastAPI app + routes (the REST layer)

4. `schemas.py` (new)
   - Pydantic models for request/response

5. `main.py` (optional)
   - starts the server or exposes `app` object cleanly

6. `tests/test_api.py` (recommended)
   - API tests using FastAPI TestClient

---

## Step-by-Step Migration Requirements (Tasks)

### 1) Setup FastAPI Project Entry Point
**Goal:** have a running server.

- Add FastAPI + ASGI server dependency (e.g., `uvicorn`).
- Create `api.py` with:
  - `app = FastAPI(title="Task Management API")`
  - a simple `GET /health` that returns `{ "status": "ok" }`

**Acceptance criteria:**
- Running `uvicorn api:app --reload` starts the server.
- `GET /health` returns HTTP 200.

---

### 2) Define Pydantic Schemas (Request/Response Models)
Create models in `schemas.py`:

- `TaskCreateRequest`: `title`, `owner`, `description` (optional)
- `TaskUpdateRequest`: optional `title`, `owner`, `description`
- `TaskStatusChangeRequest`: `new_status`
- `TaskResponse`: includes `id`, `title`, `description`, `owner`, `status`, `created_at`, `updated_at`

**Rules:**
- Validate non-empty `title` and `owner` at schema level if possible (and/or in TaskManager).
- Ensure responses are consistent types (timestamps as float or ISO string; choose one and keep consistent).

**Acceptance criteria:**
- API docs (`/docs`) show correct input/output schemas once endpoints exist.

---

### 3) Add Endpoint: Create Task (POST /tasks)
Implement:

- `POST /tasks`
- Request body: `TaskCreateRequest`
- Response: `TaskResponse`
- Status code: **201 Created**

**Behavior:**
- Calls `TaskManager.create_task(...)` (DB-backed).
- Returns created task.

**Error mapping:**
- `InvalidInputError` → HTTP 422 (or 400, but 422 is typical with validation).

---

### 4) Add Endpoint: List Tasks (GET /tasks)
Implement:

- `GET /tasks`
- Query params (optional): `status`, `owner`, `sort_by`
- Response: list of `TaskResponse`

**Behavior:**
- Pull tasks from DB using TaskManager (or repository) with filters.
- Use query parameters for filtering (RESTful style).

**Acceptance criteria:**
- `GET /tasks?owner=Ana&status=IN_PROGRESS` returns only matching tasks.

---

### 5) Add Endpoint: Get Task Details (GET /tasks/{task_id})
Implement:

- `GET /tasks/{task_id}`
- Response: `TaskResponse`

**Error mapping:**
- `TaskNotFoundError` → HTTP **404 Not Found**

---

### 6) Add Endpoint: Update Task Fields (PATCH /tasks/{task_id})
Implement:

- `PATCH /tasks/{task_id}`
- Request body: `TaskUpdateRequest` (all optional)
- Response: updated `TaskResponse`

**Rules:**
- If user sends an empty payload (no fields), return a clear error (400 or 422).
- Ensure `updated_at` is changed.

---

### 7) Add Endpoint: Change Status (POST /tasks/{task_id}/status)
Implement:

- `POST /tasks/{task_id}/status`
- Request body: `TaskStatusChangeRequest`
- Response: updated `TaskResponse`

**Rules:**
- Enforce workflow rules from your TaskManager.
- Update DB accordingly.

**Error mapping:**
- `InvalidStatusTransitionError` → HTTP **409 Conflict** (or 400; 409 is a good fit)
- `TaskNotFoundError` → 404

---

### 8) Centralize Exception Handling in FastAPI
Instead of repeating try/except in every route:

- Add FastAPI exception handlers (`@app.exception_handler(...)`) for your custom exceptions:
  - `TaskNotFoundError` → 404
  - `InvalidInputError` → 422/400
  - `InvalidStatusTransitionError` → 409

**Acceptance criteria:**
- Routes remain clean and readable.
- Errors return JSON like:
  - `{ "detail": "..." }`

---

### 9) Remove / Deprecate CLI
- The old CLI file can be removed or left for reference, but the assignment must clearly use the REST API as the main interface.
- Ensure no route relies on `input()` or `print()` for functionality.

---

### 10) API Testing (Recommended)
Create `tests/test_api.py` using `TestClient`:

Minimum tests:
- create task returns 201 and has `CREATED` status
- invalid create (empty title) returns 422/400
- get unknown task returns 404
- valid status transitions succeed
- invalid transition returns 409

**Note on DB for tests:**
- Prefer a separate test database file (e.g., `tasks_test.db`) or an in-memory approach.
- Tests should not destroy real data.

---

## Suggested REST Endpoints Summary

- `GET /health`
- `POST /tasks`
- `GET /tasks`
- `GET /tasks/{task_id}`
- `PATCH /tasks/{task_id}`
- `POST /tasks/{task_id}/status`

Optional:
- `DELETE /tasks/{task_id}`
- `GET /workflow` (returns allowed transitions)

---

## Deliverables
- A working FastAPI app (routes + schemas)
- Domain logic reused (TaskManager + workflow rules)
- SQLite-backed persistence continues to work
- Updated documentation (short README section: how to run server + how to call endpoints)
- (Recommended) API tests that pass

## How to Run (example)
- `uvicorn api:app --reload`
- Open: `http://127.0.0.1:8000/docs`