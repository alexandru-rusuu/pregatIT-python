# Homework Proposal: Error Handling and Test-Driven Refactoring of the Task Management System

## Prerequisite
This assignment is an **extension on top of** `week3/assignment1` (the Object-Oriented **Task Management System (JIRA-like)** with JSON persistence and workflow status transitions). You should **reuse and improve** that codebase.

## Estimated Implementation Time
5-9 hours

## Core Concepts to Implement
*   **Custom Exceptions:** Define and raise custom exception classes for domain-specific errors (invalid input, invalid workflow transitions, missing tasks, etc.).
*   **Comprehensive Error Handling (`try...except`):** Implement robust error handling across the application, especially for CLI input, file operations, and lifecycle transitions.
*   **Unit Testing Framework (`unittest` or `pytest`):** Write a test suite to verify the logic of the `Task` and `TaskManager` classes.
*   **Test-Driven Development (TDD) Approach (recommended):** Add tests first (or early), then refactor implementation until all tests pass.

## Project Goal
Transform your existing OOP Task Management System into a more professional-grade application by:
1) enforcing correctness through **custom exceptions** and validation
2) proving behavior via **unit tests**, including both success and failure cases.

---

## Required Structure

1.  **`task_system.py` (Existing):** Contains the `Task` and `TaskManager` classes (from assignment1).
2.  **`custom_exceptions.py` (New File):** A dedicated module for defining custom exception classes.
3.  **`test_task_manager.py` (New File):** Unit tests for the Task system.

> Note: You may keep your existing `app.py`, but it must be updated to catch and display errors cleanly.

---

## Functional Requirements (Tasks)

| Task | Concept Focus |
| :--- | :--- |
| **1. Define Custom Exceptions (`custom_exceptions.py`)** | Custom Exceptions |
| | **Description:** Create exception classes (all inherit from `Exception`) for your task domain. Minimum required: |
| | * `InvalidInputError`: Raised for invalid user/program input (empty title/owner, invalid status string, bad types, etc.). |
| | * `TaskNotFoundError`: Raised when a task ID does not exist. |
| | * `InvalidStatusTransitionError`: Raised when a status change violates the workflow rules (e.g., `CREATED` → `DONE`). |
| | **Optional (only if you implemented Undo in assignment1):** `EmptyUndoStackError` for “undo when there is nothing to undo”. |
| **2. Refactor `TaskManager` to Raise Exceptions (`task_system.py`)** | Robust Validation, Refactoring |
| | **Description:** Update `TaskManager` methods to raise your custom exceptions instead of silently failing or printing errors. Minimum behaviors: |
| | * `create_task(...)` raises `InvalidInputError` if title/owner are empty or invalid. |
| | * `get_task_by_id(...)` raises `TaskNotFoundError` (or returns `None`, but then all callers must consistently handle it; exception-based is preferred). |
| | * `update_task(...)` raises `TaskNotFoundError` for missing IDs and `InvalidInputError` for invalid updates. |
| | * `change_status(...)` raises `InvalidStatusTransitionError` for workflow violations and `TaskNotFoundError` if task not found. |
| | * `load_tasks()` handles `FileNotFoundError` and `json.JSONDecodeError` gracefully (do not crash). If you decide to raise a custom exception here, document it and handle it in `app.py`. |
| **3. Update the CLI Error Handling (`app.py`)** | Application Error Handling |
| | **Description:** Wrap user interactions with `try...except` blocks that catch your custom exceptions and print user-friendly messages. The program must continue running after errors (until user exits). |
| **4. Implement Testing Environment (`test_task_manager.py`)** | Unit Testing Setup |
| | **Description:** Create a test class (e.g., `TestTaskManager`) using `unittest.TestCase` or `pytest`. Include setup that creates a fresh `TaskManager` per test. Tests must not depend on the real JSON file (use temporary files, dependency injection, or mock I/O). |
| **5. Write Unit Tests for Core Functionality (Happy Path)** | Unit Testing |
| | **Description:** Write at least **5** tests that verify correct behavior, such as: |
| | * Creating a task sets status to `CREATED` and assigns an ID. |
| | * Updating title/description/owner changes the correct fields and updates `_updated_at`. |
| | * `change_status` works for valid transitions (e.g., `CREATED` → `IN_PROGRESS` → `IN_REVIEW` → `DONE`). |
| | * Listing/filtering returns expected tasks (if your `list_tasks` returns data; if it only prints, refactor to return a list for testability). |
| | * Saving and loading restores tasks correctly (loaded objects are valid `Task` instances or equivalent reconstructed objects). |
| **6. Write Unit Tests for Error Handling (Failure Path)** | Unit Testing + Assertions |
| | **Description:** Write at least **5** tests that confirm errors are raised correctly, such as: |
| | * Creating a task with empty title raises `InvalidInputError`. |
| | * Creating a task with empty owner raises `InvalidInputError`. |
| | * Updating a non-existent task ID raises `TaskNotFoundError`. |
| | * Changing status with an invalid transition raises `InvalidStatusTransitionError`. |
| | * Loading from invalid/corrupted JSON does not crash the app (either handled internally or raises a documented exception). |
| | **Optional (only if Undo exists):** Undo with an empty stack raises `EmptyUndoStackError` (or is handled gracefully, but must be consistent and tested). |

---

## Suggested Implementation Steps

1.  Create `custom_exceptions.py` and define required exceptions.
2.  Refactor `task_system.py` to validate inputs and raise exceptions consistently.
3.  Refactor any “print-only” methods so they also return values (to make testing easier).
4.  Create `test_task_manager.py` and write happy-path tests first.
5.  Add failure-path tests to ensure invalid inputs and invalid transitions are handled correctly.
6.  Update `app.py` to catch custom exceptions and keep the CLI running smoothly.
7.  Run the full test suite until everything passes.

---
## Deliverables
* `custom_exceptions.py`
* `test_task_manager.py`
* Updated `task_system.py` (refactored to raise exceptions)
* Updated `app.py` (handles exceptions cleanly)
* A short note in the README or as comments describing how to run tests (`python -m unittest` or `pytest`)