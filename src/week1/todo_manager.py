if __name__ == "__main__":
    tasks: list[str] = []

    while True:
        print("\n--- to-do list manager ---")
        print("1. add task")
        print("2. view tasks")
        print("3. delete task")
        print("4. exit")

        choice: str = input("choose an option: ")

        if choice == '1':
            task: str = input("enter task description: ").strip()
            if task:
                tasks.append(task)
                print(f"added: {task}")
            else:
                print("error: task description cannot be empty!")
        elif choice == '2':
            if not tasks:
                print("the list is empty.")
            else:
                [print(f"{i+1}. {t}") for i, t in enumerate(tasks)]
        elif choice == '3':
            if not tasks:
                print("no tasks to delete.")
            else:
                try:
                    idx: int = int(input("enter task number to delete: "))
                    removed: str = tasks.pop(idx - 1)
                    print(f"successfully deleted: {removed}")
                except (ValueError, IndexError):
                    print("invalid task number!")
        elif choice == '4':
            print("goodbye!")
            break
        else:
            print("invalid choice, try again.")