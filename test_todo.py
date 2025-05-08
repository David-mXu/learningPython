import pytest

from todo import Task, TaskManager, Subcategory, Category
import datetime

def create_task():
    task = Task("Do HW", "for ECE140, problem set 1", datetime.datetime.now(), 1)
    assert task.taskTitle == "Do HW"
    assert task.taskDescription == "for ECE140, problem set 1"
    assert task.dueDate == datetime.datetime.now()
    assert task.priority == 1

def complete_task():
    task = Task("Do HW", "for ECE140, problem set 1", datetime.datetime.now(), 1)
    task.mark_complete()
    assert task.complete is True

@pytest.fixture
def sample_todolist():
    taskManager = TaskManager()
    #testing for tasks based in the task manager group
    taskManager.add_task("Apply Co-op jobs", "On Waterlooworks & Linkedin", datetime.date.today() + datetime.timedelta(days=1), 1)
    taskManager.add_task("Do HW", "for ECE124, check outline for hw", datetime.datetime.now(), 1)
    #creating cases for category group
    taskManager.add_category("Personal Projects")
    taskManager.add_category("School")
    taskManager.add_category("Project Management")

    #creating cases for subcategory group





