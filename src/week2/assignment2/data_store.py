EVENT_LOG: list[dict] = []
UNDO_STACK: list[int] = []


def add_event(event_id: int, name: str, priority: str = 'LOW', **kwargs) -> None:
    new_event = {
        'id': event_id,
        'name': name,
        'priority': priority,
    }
    new_event.update(kwargs)

    global EVENT_LOG
    EVENT_LOG.append(new_event)