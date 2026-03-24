from task_system import TaskManager, Task
from custom_exceptions import InvalidInputError, TaskNotFoundError, InvalidStatusTransitionError, EmptyUndoStackError

if __name__ == "__main__":
    manager: TaskManager = TaskManager()
    manager.load_tasks()

    while True:
        print("\n--- JIRA-lite Task Manager ---")
        print("1. create Task")
        print("2. list Tasks")
        print("3. view Task Details")
        print("4. update Task")
        print("5. change Status")
        print("6. undo Last Action")
        print("7. save")
        print("8. exit")

        choice: str = input("choose an option: ")

        try:
            if choice == '1':
                title: str = input("title: ")
                owner: str = input("owner: ")
                desc: str = input("description: ")
                manager.create_task(title, owner, desc)
                print("task created.")

            elif choice == '2':
                status_filter: str = input("filter by status (leave empty for all): ") or None
                owner_filter: str = input("filter by owner (leave empty for all): ") or None
                sort_field: str = input("sort by (id, title, owner, status, updated_at) [default id]: ") or "id"
                tasks: list[Task] = manager.list_tasks(status_filter, owner_filter, sort_field)
                [print(t) for t in tasks]

            elif choice == '3':
                t_id: int = int(input("task ID: "))
                task: Task = manager.get_task_by_id(t_id)
                print("=" * 20)
                [print(f"{k.lstrip('_')}: {v}") for k, v in task.to_dict().items()]
                print("=" * 20)

            elif choice == '4':
                t_id: int = int(input("task ID: "))
                title: str = input("new Title (leave empty to skip): ") or None
                owner: str = input("new Owner (leave empty to skip): ") or None
                desc: str = input("new Description (leave empty to skip): ") or None
                manager.update_task(t_id, title, owner, desc)
                print("task updated.")

            elif choice == '5':
                t_id: int = int(input("task ID: "))
                new_status: str = input("new Status (CREATED, IN_PROGRESS, BLOCKED, DONE): ")
                manager.change_status(t_id, new_status)
                print("status updated.")

            elif choice == '6':
                manager.undo_last_action()
                print("undo successful.")

            elif choice == '7':
                manager.save_tasks()
                print("tasks saved to JSON.")

            elif choice == '8':
                manager.save_tasks()
                print("tasks saved. Goodbye!")
                break

            else:
                print("invalid choice. Try again.")

        except ValueError:
            print("input error: please enter a valid number for ID.")
        except InvalidInputError as e:
            print(f"validation error: {e}")
        except TaskNotFoundError as e:
            print(f"not found: {e}")
        except InvalidStatusTransitionError as e:
            print(f"workflow error: {e}")
        except EmptyUndoStackError as e:
            print(f"undo error: {e}")
        except Exception as e:
            print(f"unexpected error: {e}")