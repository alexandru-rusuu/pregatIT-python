# Final Assignment: Migrate and Containerize the Task Management System

## Overview
This final assignment is the culmination of the Python course. You will take the **Task Management System** (from Week 3 and 4) and transform it into a professional, production-ready, containerized application using **FastAPI** and **PostgreSQL**.

The goal is to move away from a local SQLite `.db` file and a simple CLI/local API, to a fully orchestrated environment where the database and the application run in separate Docker containers.

---

## Core Requirements

### 1. Database Migration (SQLite to PostgreSQL)
- Migrate the persistence layer from the local SQLite `tasks.db` file to a **containerized PostgreSQL database**.
- Adapt your database connection logic (e.g., in `db_handler.py` or `TaskManager`) to use PostgreSQL connection strings.
- Ensure the application reads database credentials (host, port, user, password, db name) from environment variables or a configuration file (e.g., `config.properties` or `.env`).

### 2. API Containerization
- Containerize the **FastAPI layer** of your Task Management System.
- Create a `Dockerfile` for the application that:
  - Uses an appropriate Python base image.
  - Installs all necessary dependencies (including PostgreSQL drivers like `psycopg2`).
  - Sets up the `PYTHONPATH` correctly.
  - Launches the application using a production-grade server like `gunicorn` with `uvicorn` workers.

### 3. Docker Orchestration
- Create a `docker-compose.yml` file to manage both the **APP layer** and the **DB layer**.
- The `docker-compose.yml` must:
  - Define two independent services: `db` (PostgreSQL) and `app` (FastAPI).
  - Use environment variables for database configuration.
  - Ensure the `app` container **depends on** the `db` container at startup.
  - Persist PostgreSQL data using a Docker volume.

---

## Quality & Implementation Standards

Your final project will be evaluated based on the following six strict requirements:

1.  **Show good usage of OOP patterns:**
    - Maintain a clear separation of concerns (Model, Service/Logic, Repository/DB layer).
    - Use classes (`Task`, `TaskManager`, etc.) effectively with proper encapsulation and inheritance where applicable.

2.  **RESTful API Endpoints:**
    - Implement a complete set of RESTful endpoints for all task operations:
      - `POST /tasks` (Create)
      - `GET /tasks` (List with filtering by status/owner)
      - `GET /tasks/{id}` (Read details)
      - `PATCH /tasks/{id}` (Update fields)
      - `POST /tasks/{id}/status` (Workflow transition)
      - `DELETE /tasks/{id}` (Delete)
    - Use appropriate HTTP methods, status codes (200, 201, 204, 404, 409, etc.), and Pydantic models for validation.

3.  **PEP8 Standards:**
    - Ensure all code adheres to PEP8 standards for linting and formatting.
    - Use meaningful names, consistent indentation, and proper import ordering.

4.  **Independent Docker Containers:**
    - The DB and APP layers must run in separate containers.
    - The APP must wait for/depend on the DB to be ready before fully starting its services.

5.  **Automatic DB Initialization:**
    - On application startup, the system must automatically detect if the required table structure exists in PostgreSQL.
    - If the tables do not exist, the application must **initialize the DB** (create the schema) before accepting requests.

6.  **Test Coverage (80% minimum):**
    - Achieve at least **80% test coverage** across the API, Service (business logic), and Repository (database) layers.
    - Use `pytest` or `unittest` with coverage tools to verify this.

---

## Suggested Deliverables
- `task_system.py` / `db_handler.py` (Adapted for PostgreSQL)
- `api.py` / `schemas.py` (FastAPI implementation)
- `Dockerfile`
- `docker-compose.yml`
- `config.properties` or `.env` template
- `tests/` directory with comprehensive test suites
- `requirements.txt` listing all dependencies

---

## Evaluation
Your work will be judged on the robustness of the containerized setup, the cleanliness of the OOP design, the RESTful correctness of the API, and the quality of your automated tests.
