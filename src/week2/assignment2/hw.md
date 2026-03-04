# Homework Proposal: Procedural Log and Processor with Stack & Queue

## Estimated Implementation Time
4-6 hours

## Core Concepts to Implement
*   **Functions & Parameters:** Utilize positional, keyword, and default parameters in function definitions.
*   **Variable Scope:** Manage core data structures as module-level global variables.
*   **Lambda Functions:** Use a `lambda` function for quick data manipulation (e.g., sorting).
*   **Modules:** Structure the project into at least two separate Python files and use the `import` statement.
*   **Advanced Data Structure - Queue (FIFO):** Implement a custom Queue using a standard Python `list` to manage the primary event log.
*   **Advanced Data Structure - Stack (LIFO):** Implement a custom Stack using a standard Python `list` for an "Undo" feature.

## Project Description
You will create a fully procedural Command-Line Interface (CLI) application that simulates an **"In-Memory Event Processing System."** Events are added to the main log (Queue) and processed in order. The application also supports an **Undo** feature for the latest action using a Stack. All data is managed in-memory and will not persist after the program exits.

### Required Structure

1.  **`data_store.py` (Module):** This file contains the module-level data structures (our "in-memory database") and simple utility functions for adding and listing.
    *   **Module-Level Variables:**
        *   `EVENT_LOG`: The main list of event dictionaries (acts as the **Queue**).
        *   `UNDO_STACK`: A list to store the ID of the last added event (acts as the **Stack**).

2.  **`app.py` (Main Script):** This file contains the main application loop, the user interface logic, and the functions that implement the Queue and Stack processing logic.

### Functional Requirements (Tasks)

| Task | Module Concept Focus |
| :--- | :--- |
| **1. Event Creation (`data_store.py`)** | Functions, Parameters, Global Scope |
| | **Description:** Implement `add_event(name: str, priority: str = 'LOW', **kwargs)` to create a new event dictionary (must include a unique `id`, `name`, and `priority`). This function must append the new event dictionary to the module-level `EVENT_LOG` list. Use `**kwargs` for optional notes. |
| **2. Queue Processing (`app.py`)** | Queue Implementation (FIFO), Functions |
| | **Description:** Implement `process_next_event()` that removes and prints the **oldest** event from the `EVENT_LOG` list (Queue's **Dequeue**). If the list is empty, print a message. |
| **3. Stack Management (`app.py`)** | Stack Implementation (LIFO), Global Scope |
| | **Description:** Implement a function `push_to_undo(event_id)` that adds the `event_id` to the `UNDO_STACK` (Stack's **Push**). This function will be called immediately after a new event is added. |
| **4. Undo Functionality (`app.py`)** | Stack Implementation (LIFO), Global Scope |
| | **Description:** Implement `undo_last_event()` that retrieves and removes the last ID from the `UNDO_STACK` (Stack's **Pop**). Use this ID to locate and remove the corresponding event from the `EVENT_LOG`. If the stack is empty, print a message. |
| **5. Listing with Lambda (`app.py`)** | Lambda Functions, Default Parameters |
| | **Description:** Implement `list_events(sort_by: str = 'id')`. This function prints all events in the `EVENT_LOG`. Use a **lambda function** as the key for Python's built-in `sorted()` function to allow sorting by `id`, `name`, or `priority`. |
| **6. Main Application Loop (`app.py`)** | Modules, Procedural Design |
| | **Description:** Implement a simple loop to present the user with a menu (Add Event, Process Next, Undo, List All, Exit) and call the corresponding functions from the imported module (`data_store.py`) or local functions. |

### Suggested Implementation Steps

1.  **Setup:** Create the project directory, `data_store.py`, and `app.py`.
2.  **`data_store.py`:**
    *   Initialize the `EVENT_LOG` and `UNDO_STACK` lists.
    *   Implement `add_event`, ensuring it handles `**kwargs` and appends to `EVENT_LOG`.
3.  **`app.py` (Setup):**
    *   Import necessary variables and functions from `data_store.py` (e.g., `from data_store import EVENT_LOG, UNDO_STACK, add_event`).
    *   Implement `push_to_undo` and the main menu loop.
4.  **`app.py` (Logic):**
    *   Implement `process_next_event` (Queue logic: `pop(0)`).
    *   Implement `undo_last_event` (Stack logic: `pop()` on `UNDO_STACK`, then locate and remove from `EVENT_LOG`).
    *   Implement `list_events` using a `lambda` function for the sort key.
