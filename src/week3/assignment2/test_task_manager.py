import unittest
import os
from task_system import TaskManager, Task
from custom_exceptions import InvalidInputError, TaskNotFoundError, InvalidStatusTransitionError, EmptyUndoStackError

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.test_filename: str = "test_tasks.json"
        self.manager: TaskManager = TaskManager(self.test_filename)

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_create_task_happy(self):
        task: Task = self.manager.create_task("Test Title", "Test Owner")
        self.assertEqual(task._status, "CREATED")
        self.assertIsNotNone(task._id)
        self.assertEqual(len(self.manager.tasks), 1)

    def test_update_task_happy(self):
        task: Task = self.manager.create_task("Test Title", "Test Owner")
        self.manager.update_task(task._id, title="New Title", description="New Desc")
        updated_task: Task = self.manager.get_task_by_id(task._id)
        self.assertEqual(updated_task._title, "New Title")
        self.assertEqual(updated_task._description, "New Desc")

    def test_change_status_happy(self):
        task: Task = self.manager.create_task("Test Title", "Test Owner")
        self.manager.change_status(task._id, "IN_PROGRESS")
        self.assertEqual(task._status, "IN_PROGRESS")

    def test_list_tasks_happy(self):
        self.manager.create_task("T1", "User1")
        self.manager.create_task("T2", "User2")
        tasks: list[Task] = self.manager.list_tasks(filter_owner="User1")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]._title, "T1")

    def test_save_and_load_happy(self):
        self.manager.create_task("Load Test", "Loader")
        self.manager.save_tasks()
        new_manager: TaskManager = TaskManager(self.test_filename)
        new_manager.load_tasks()
        self.assertEqual(len(new_manager.tasks), 1)
        self.assertEqual(new_manager.tasks[0]._title, "Load Test")

    def test_create_task_empty_title_fails(self):
        with self.assertRaises(InvalidInputError):
            self.manager.create_task("", "Test Owner")

    def test_create_task_empty_owner_fails(self):
        with self.assertRaises(InvalidInputError):
            self.manager.create_task("Test Title", "   ")

    def test_update_nonexistent_task_fails(self):
        with self.assertRaises(TaskNotFoundError):
            self.manager.update_task(999999, title="New")

    def test_change_status_invalid_transition_fails(self):
        task: Task = self.manager.create_task("Test Title", "Test Owner")
        with self.assertRaises(InvalidStatusTransitionError):
            self.manager.change_status(task._id, "BLOCKED")

    def test_empty_undo_stack_fails(self):
        with self.assertRaises(EmptyUndoStackError):
            self.manager.undo_last_action()

if __name__ == "__main__":
    unittest.main()