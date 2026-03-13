# Homework Proposal: Object-Oriented Task Management System (JIRA-like)

## Estimated Implementation Time
4-7 hours

## Core Concepts to Implement (OOP Increment)

*   **Object-Oriented Programming (OOP):** Define classes (`Event`, `EventManager`) with attributes and methods.
*   **Encapsulation/Special Methods:** Use private-like attributes (conventionally with `_`) and implement the `__str__` method for clean output.
*   **Error Handling:** Use `try...except` blocks for file operations and user input validation.
*   **File I/O (JSON):** Implement methods to save and load the list of `Event` objects to/from a **JSON file**.
*   **Advanced Data Structure Integration:** The `EventManager` class will manage the primary event **Queue** and the **Stack** for the undo feature.

## Project Description
You will build a fully object-oriented command-line application that manages **Task objects**. Users can create tasks with an owner and description, then move tasks through a controlled lifecycle from **Created** until **Done**. Data must persist between runs using a JSON file.

### Required Structure

1.  **`task_system.py` (Classes and Logic):** This file will contain both core classes.
    *   **`Task` Class:** Represents a single task (like a JIRA ticket).
    *   **`TaskManager` Class:** Manages the list of tasks and all application logic (CRUD, workflow, File I/O).

2.  **`app.py` (Main Script):** Contains the application's entry point, the main menu loop, and error handling for user interaction.

### Functional Requirements (Tasks)

| Task | Module Concept Focus |
| :--- | :--- |
| **1. `Task` Class Implementation** | OOP, `__init__`, Encapsulation, `__str__` |
| | **Description:** Must have attributes for `_id`, `_title`, `_description`, `_owner`, `_status`, `_created_at`, and `_updated_at`. Implement a constructor (`__init__`) that assigns a unique ID and sets timestamps. New tasks must start with status `CREATED`. Implement `__str__` to return a user-friendly string representation. |
| **2. `TaskManager` Class Setup** | OOP, Data Structure Management |
| | **Description:** Implement an `__init__` constructor that initializes `self.tasks` (the primary list of `Task` objects). If you implement Undo (optional), also initialize `self.undo_stack`. |
| **3. File Persistence Methods** | File I/O, Error Handling, JSON |
| | **Description:** Within `TaskManager`, implement `load_tasks()` and `save_tasks()`. Use the built-in `json` module. `load_tasks()` must handle `FileNotFoundError` (start with an empty list) and `json.JSONDecodeError` (corrupted files). **Note:** You must convert `Task` objects to dictionaries before saving and convert dictionaries back to `Task` objects after loading. |
| **4. Core Task Operations (CRUD-lite)** | Method Implementation, Input Validation |
| | **Description:** Implement these methods inside `TaskManager`: |
| | *   **Create:** `create_task(title: str, owner: str, description: str = "")` creates a new `Task` and appends it to `self.tasks`. |
| | *   **Read/List:** `list_tasks(filter_status: str = None, filter_owner: str = None, sort_by: str = "id")` prints tasks. Sorting should use a `lambda` and allow sorting by `id`, `owner`, `status`, or `updated_at`. |
| | *   **Update:** `update_task(task_id: int, title: str = None, owner: str = None, description: str = None)` updates fields and refreshes `_updated_at`. |
| | *   **Details:** `get_task_by_id(task_id: int)` returns the task (or `None`) to support a “View Task Details” menu option. |
| **5. Status Change / Workflow Enforcement** | Control Flow, Domain Rules |
| | **Description:** Implement `change_status(task_id: int, new_status: str)` that updates the task’s status **only if** the transition is allowed by the workflow rules. If not allowed, raise an error or print a message and do nothing. Always update `_updated_at` on successful status change. |
| **6. Main Application Loop (`app.py`)** | Error Handling, Module Integration |
| | **Description:** In `app.py`, instantiate `TaskManager` and call `load_tasks()`. Implement a menu for user interaction: Create Task, List Tasks, View Task, Update Task, Change Status, Save, Exit. Use `try...except` to handle invalid IDs, invalid statuses, and invalid transitions without crashing. |
| **7. (Optional) Undo Last Change** | Stack (LIFO), State Management |
| | **Description:** Implement an optional undo feature (like “oops”). You may store previous task snapshots or action records in `self.undo_stack`. Provide `undo_last_action()` in `TaskManager` and add a menu option for it. If the stack is empty, show a friendly message. |

## Suggested Implementation Steps

1.  **Setup:** Create `task_system.py` and `app.py`.
2.  **`task_system.py` (Task Class):** Define `Task`. Generate unique IDs (e.g., `time.time()` or an incrementing counter loaded from file) and store timestamps.
3.  **`task_system.py` (Manager Class - Basic):** Define `TaskManager`, implement `create_task`, `get_task_by_id`, and `list_tasks`.
4.  **Workflow:** Implement and test `change_status` using the allowed transitions table.
5.  **File I/O:** Implement `save_tasks` and `load_tasks` (object ↔ dict conversion).
6.  **`app.py` (Loop):** Implement the main loop and menu. Validate user input.
7.  **(Optional) Undo:** Add `undo_last_action` and integrate it into the menu.
8.  **Review:** Test: create tasks, edit fields, move through statuses from `CREATED` to `DONE`, save and reload to confirm persistence.