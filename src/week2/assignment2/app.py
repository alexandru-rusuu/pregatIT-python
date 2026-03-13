from data_store import EVENT_LOG, UNDO_STACK, add_event


def push_to_undo(event_id: int) -> None:
    UNDO_STACK.append(event_id)


def process_next_event() -> None:
    if not EVENT_LOG:
        print("no events to process.")
        return

    # FIFO: pop(0) removes the first element added
    event = EVENT_LOG.pop(0)
    print(f"processed event: {event}")


def undo_last_event() -> None:
    if not UNDO_STACK:
        print("nothing to undo.")
        return

    last_id = UNDO_STACK.pop()

    global EVENT_LOG
    for i, event in enumerate(EVENT_LOG):
        if event['id'] == last_id:
            EVENT_LOG.pop(i)
            print(f"undone event with id: {last_id}")
            return
    print("event not found in log.")


def list_events(sort_by: str = 'id') -> None:
    if not EVENT_LOG:
        print("the log is empty.")
        return

    sorted_list = sorted(EVENT_LOG, key=lambda x: x.get(sort_by, 0))

    print(f"\n--- events sorted by {sort_by} ---")
    for e in sorted_list:
        print(e)


def main_menu() -> None:
    current_id = 1

    while True:
        print("\n--- event system menu ---")
        print("1. add event")
        print("2. process next (queue)")
        print("3. undo last (stack)")
        print("4. list all")
        print("5. exit")

        choice: str = input("choose an option: ")

        if choice == '1':
            name: str = input("enter event name: ")
            priority: str = input("enter priority (LOW/MED/HIGH): ") or "LOW"
            note: str = input("enter a quick note (optional): ")

            add_event(current_id, name, priority, notes=note)
            push_to_undo(current_id)
            print(f"event added with id {current_id}")
            current_id += 1

        elif choice == '2':
            process_next_event()

        elif choice == '3':
            undo_last_event()

        elif choice == '4':
            sort_key: str = input("sort by (id/name/priority): ") or "id"
            list_events(sort_key)

        elif choice == '5':
            print("exiting program...")
            break
        else:
            print("invalid option, try again.")


if __name__ == "__main__":
    main_menu()