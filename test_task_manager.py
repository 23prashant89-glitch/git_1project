import unittest
import os
from task_manager import (
    add_task,
    remove_tasks,
    load_tasks,
    list_tasks,
    TASKS_FILE,
)


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        if os.path.exists(TASKS_FILE):
            os.remove(TASKS_FILE)

    def test_add_task(self):
        result = add_task("Buy Milk")
        # result should confirm the added task
        self.assertEqual(result, 'Task "Buy Milk" added.')
        # the stored tasks should include the added task
        self.assertIn("Buy Milk", load_tasks())

    def test_remove_task(self):
        add_task("Buy Eggs")
        result = remove_tasks("Buy Eggs")
        # result should confirm the removed task
        self.assertEqual(result, 'Task "Buy Eggs" removed.')
        # after removal, the task should no longer be present
        self.assertNotIn("Buy Eggs", load_tasks())

    def test_list_tasks_empty(self):
        result = list_tasks()
        self.assertEqual(result, "No tasks found.")

    def test_list_tasks_with_items(self):
        add_task("Task 1")
        add_task("Task 2")
        result = list_tasks()
        self.assertIn("1. Task 1", result)
        self.assertIn("2. Task 2", result)

    def test_remove_nonexistent_task(self):
        result = remove_tasks("Nonexistent Task")
        self.assertIn("not found", result)

    def tearDown(self):
        if os.path.exists(TASKS_FILE):
            os.remove(TASKS_FILE)


if __name__ == "__main__":
    unittest.main()
