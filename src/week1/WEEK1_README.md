# Python Practice Exercises

## 1. Basic Syntax, Data Types, user input and output

Create a simple program that gathers user's data:
 - birthday (day, month, year)
 - name
 - Country

Based on this user data, decide if user is old enough to drive and vote in their country:
 - Example input: 
   - birthdate DD/MM/YYYY: 01.02.2000
   - name: Ion Ionescu
   - country: Romania

 - Example output: 
   - Congratulations, Ion Ionescu, you are old enough to vote in Romania!
   - Congratulations, Ion Ionescu, you are old enough to drive in Romania!

 - Hints:
   - For the sake of simplicity, do not split code into functions for now, we'll do that later.
   - Remember to keep it simple and have default cases where input is unknown
   - Add validations for input data (ex. if provided birthday data is not a 'natural' number, out of bounds (ex. month >12 ) etc.)
   - Remember to use the concepts within the presentation.
   - Comprehensions might help you

###

# Homework Proposal: Python To-Do List Manager

**Based on Course Material:** Module 1: Introduction to Python and Control Structures (Covers Basic Syntax, Data Types, I/O, Control Structures, Loops, and Comprehensions)

**Estimated Time to Implement:** 4-6 hours

## Objective

Create a simple command-line To-Do List Manager application in Python that allows a user to perform basic operations on a list of tasks.

## Requirements

1.  **Main Loop and Control Flow:**
    *   The application must run continuously until the user explicitly chooses to exit (e.g., using a `while` loop).
    *   Implement a main menu with options for the user. Use `if-elif-else` statements to process the user's choice (e.g., '1' for Add, '2' for View, '3' for Delete, '4' for Exit).

2.  **Data Storage and Types:**
    *   Use a Python `list` to store the to-do items.
    *   Each to-do item should be stored as a string.

3.  **Input and Output (I/O):**
    *   Use the `input()` function to capture the user's menu choice and task details (e.g., the name of the task to add or the index of the task to delete).
    *   Use the `print()` function with f-strings (the preferred method) to display the menu, task list, and confirmation messages.

4.  **Core Functionality:**
    *   **Add Task:** Prompt the user for a task description and add it to the list.
    *   **View Tasks:** Display the current list of tasks, numbering each item. Use a `for` loop to iterate through the list. If the list is empty, display a message.
    *   **Delete Task:** Prompt the user for the number of the task to delete and remove it from the list. Include error handling for invalid input (e.g., non-existent task number).
    *   **Exit:** Terminate the program execution (e.g., by using the `break` statement to exit the main loop).

## Bonus Challenges (Optional)

To practice more advanced concepts from the module:

*   **Task Status (Dictionary Comprehension):** Instead of a simple list of strings, use a `list` of `dictionaries`. Each dictionary should have keys like `"task"` and `"status"` (e.g., "Pending" or "Complete"). Implement a new menu option to change a task's status.
*   **Filter Tasks (List Comprehension):** Implement a feature to view only "Pending" or only "Complete" tasks using a **list comprehension** to filter the main task list.