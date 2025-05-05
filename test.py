import unittest
from todo import Task, TaskManager, Category, Subcategory

class TestTask(unittest.TestCase):
    def setUp(self):
        self.taskTitle = "taskTitle"
        self.taskDescription = "taskDescription"
        self.dueDate = "dueDate"
        self.priority = 1
        self.complete = False

    def test_task_completion(self):
        self.assertEqual(True, False)  # add assertion here

class TestTaskManager(unittest.TestCase):
    pass

class TestCategory(unittest.TestCase):
    pass

class TestSubcategory(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
