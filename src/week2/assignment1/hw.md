# Homework Proposal: Modular Command-Line Contact Manager

## Estimated Implementation Time
4-6 hours

## Core Module 2 Concepts to Implement
*   **Defining Functions:** Use the `def` keyword and include type hints for all function signatures.
*   **Parameter Types:** Utilize positional, keyword, and default parameters in different functions.
*   **Variable-Length Arguments:** Implement `*args` and `**kwargs` in at least one function.
*   **Variable Scope:** Demonstrate an understanding of local and global scope (e.g., managing the main contacts list).
*   **Lambda Functions:** Use a `lambda` function for a simple data manipulation task (e.g., sorting).
*   **Modules:** Structure the project into at least two separate Python files and use the `import` statement.

## Project Description
You will create a simple Command-Line Interface (CLI) application that allows a user to manage a list of contacts. The contacts will be stored in a Python list of dictionaries (for simplicity, no file persistence is required).

### Required Structure

1.  **`contact_manager.py` (Module):** This file will contain all the core business logic functions.
    *   **`contacts` list:** Initialize a list of dictionaries (e.g., `[{'name': '...', 'phone': '...', 'email': '...'}, ...]`) at the module level. This represents the "database."

2.  **`app.py` (Main Script):** This file will contain the main application loop, the user interface logic, and will **import** and use the functions from `contact_manager.py`.

### Functional Requirements (Tasks)

| Task | Module 2 Concept Focus |
| :--- | :--- |
| **1. `add_contact(name: str, phone: str, **kwargs: dict)`** | Function Definition, Positional & Keyword Args, `**kwargs` |
| | **Description:** Adds a new contact dictionary to the global `contacts` list. Must accept `name` and `phone` as mandatory positional arguments. Use `**kwargs` to allow for optional fields like `email`, `company`, or `notes`. |
| **2. `list_all_contacts(sort_key: str = 'name', reverse: bool = False)`** | Default Parameters, Lambda Functions |
| | **Description:** Prints all contacts. The function must use `sort_key` (defaulting to `'name'`) and `reverse` (defaulting to `False`) as default parameters to sort the list. Use a **lambda function** as the key for the `sort()` method. |
| **3. `search_contacts(*args, **kwargs)`** | `*args` and `**kwargs` Usage |
| | **Description:** Searches the `contacts` list. If `*args` are provided, search for contacts whose name or phone number *starts with* the string in `*args` (handle multiple search terms in `*args`). If `**kwargs` are provided (e.g., `email='example@'`), search for exact matches on those keyword fields. Print the results. |
| **4. `display_contact_details(contact: dict)`** | Function Definition, Positional Args |
| | **Description:** A simple utility function that takes a single contact dictionary and formats its details neatly for printing. |
| **5. Main Loop (in `app.py`)** | Modules, Imports, Variable Scope |
| | **Description:** Implement a simple loop to present the user with a menu (Add, List, Search, Exit) and call the corresponding functions from the `contact_manager` module. |

### Suggested Implementation Steps

1.  **Setup:** Create the project directory, `contact_manager.py`, and `app.py`.
2.  **`contact_manager.py`:**
    *   Initialize the `contacts` list.
    *   Implement `display_contact_details`.
    *   Implement `add_contact`, ensuring it handles `**kwargs`.
    *   Implement `list_all_contacts` using a lambda function for sorting.
3.  **`app.py`:**
    *   Import necessary functions from `contact_manager.py` (e.g., `from contact_manager import add_contact, list_all_contacts`).
    *   Implement the main menu loop.
    *   Add some initial data using `add_contact` before the loop starts.
4.  **`contact_manager.py` (Advanced):**
    *   Implement `search_contacts` to fully utilize `*args` and `**kwargs` for flexible searching.
5.  **Review:** Test all functions and ensure your code is well-commented and uses type hints (best practice).