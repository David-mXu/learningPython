#libraries I prob got to use
from datetime import datetime
from datetime import timedelta

class Task: #setting up tasks
    def __init__(self, taskTitle, taskDescription, dueDate, priority):
        self.taskTitle = taskTitle
        self.taskDescription = taskDescription
        self.dueDate = dueDate.today()
        self.priority = priority
        self.complete = False

    #for reference
    def taskTitle(self):
        return self.taskTitle
    def taskDescription(self):
        return self.taskDescription
    def priority(self):
        return self.priority
    def dueDate(self):
        return self.dueDate
    def complete(self):
        return self.complete

    def mark_complete(self):
        self.complete = True

    @property
    def __str__(self):
        return self.taskTitle + ': ' + self.taskDescription + " (" + self.priority + ")" + " " + str(self.dueDate)

class Subcategory:
    def __init__(self, subcategoryTitle):
        self.subcategoryTitle = subcategoryTitle
        self.tasks = []

    def add_task(self, Title, Description, dueDate, priority):
        new_task = Task(Title, Description, dueDate, priority)
        self.tasks.append(new_task)
        
    def sort_tasks(self):
        # sorting using lambda allows me to sort by specific keys, and a tuple in this case acts as a key that can hold multiple items
        self.tasks.sort(key=lambda task: (task.dueDate, task.priority))
        
        
class Category:
    def __init__(self, categoryTitle):
        self.categoryTitle = categoryTitle
        self.subcategories = []
        self.tasks = []
        
    def add_subcategory(self, subcategoryTitle):
        self.subcategories.append(subcategoryTitle)
    
    def add_task(self, Title, Description, dueDate, priority):
        new_task = Task(Title, Description, dueDate, priority)
        self.tasks.append(new_task)
        
    def sort_tasks(self):
        # sorting using lambda allows me to sort by specific keys, and a tuple in this case acts as a key that can hold multiple items
        self.tasks.sort(key=lambda task: (task.dueDate, task.priority))
        
    def complete_task(self, number): #make sure that we distinguish completed and uncompleted tasks, but not delete completed tasks (so can view completed)
        self.tasks[number-1].mark_complete()
        print(f"Task #{number}: {self.tasks[number-1].taskTitle()} is complete!")

    def delete_task(self, number): # make sure that we have the chance to acc remove tasks
        boolean = False
        for index in range(len(self.tasks)):  # iterate through the indicies of the list
            if number - 1 == index:
                boolean = True
                break
        if boolean:
            del self.tasks[number-1]
            print("Task Deleted!")
        else:
            print("You did not choose an existing task.")

    def delete_subcategory(self, number):
        pass

class TaskManager: # how the tasks will be arranged and managed (prioritization, adding, viewing, deleting etc...)
    def __init__(self):
        self.categories = []
        self.tasks = [] # the list that stores our tasks

    def add_task(self, Title, Description, dueDate, priority):
        new_task = Task(Title, Description, dueDate, priority)
        self.tasks.append(new_task)

    def sort_tasks(self):
        # sorting using lambda allows me to sort by specific keys, and a tuple in this case acts as a key that can hold multiple items
        self.tasks.sort(key=lambda task: (task.dueDate, task.priority))

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet")
        else:
            for number, tasks in enumerate(self.tasks):
                print(f"{number + 1}. {tasks.taskTitle}, P{tasks.priority}")
                print(tasks.taskDescription)
                print()

    def complete_task(self, number): #make sure that we distinguish completed and uncompleted tasks, but not delete completed tasks (so can view completed)
        self.tasks[number-1].mark_complete()
        print(f"Task #{number}: {self.tasks[number-1].taskTitle()} is complete!")

    def delete_task(self, number): # make sure that we have the chance to acc remove tasks
        boolean = False
        for index in range(len(self.tasks)):  # iterate through the indicies of the list
            if number - 1 == index:
                boolean = True
                break
        if boolean:
            del self.tasks[number-1]
            print("Task Deleted!")
        else:
            print("You did not choose an existing task.")

    def delete_category(self):
        pass

class HelpUserTo: #created this to simplify and clean up main code, also helping me with understanding of OOP
    def __init__(self):
        self.taskManager = TaskManager()

    def create_task(self):
        taskTitle = input("Enter Task: ")
        taskDescription = input("Enter Description (Enter to skip): ")
        taskDueDate = input("Enter Task Due Date (Enter to skip + default = today): ")
        taskPriority = int(input("Enter Task Priority (Enter to skip): "))
        if not (4 >= taskPriority >= 1):
            raise ValueError("Priority must be between 1 and 4")
        self.taskManager.add_task(taskTitle, taskDescription, taskPriority)

    def delete_task(self):
        self.taskManager.view_tasks()
        delete = int(input("Choose an existing task to delete (1,2,3,... ->): "))
        self.taskManager.delete_task(delete)

    def see_tasks(self):
        self.taskManager.view_tasks()



if __name__ == "__main__":

        helpUserTo = HelpUserTo()
        while True: # replacing this code with an OOP approach to apply OOP skills. Now this will be my interactive UI thing.

            user = input("Press '1' to create a new task, '2' to delete an existing task, '3' to see all tasks, '4' to create a project, '5' to create a section to a project, '0' to quit.")
            if user == '1':
                helpUserTo.create_task()
            if user == '2':
                helpUserTo.delete_task()
            if user == '3':
                helpUserTo.see_tasks()
            if user == '0':
                break

