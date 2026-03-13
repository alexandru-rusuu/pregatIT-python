class InvalidInputError(Exception):
    pass

class TaskNotFoundError(Exception):
    pass

class InvalidStatusTransitionError(Exception):
    pass

class EmptyUndoStackError(Exception):
    pass