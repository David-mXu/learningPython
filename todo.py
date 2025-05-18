#libraries I prob got to use
from datetime import datetime
from datetime import timedelta

class Task: #setting up tasks
    def __init__(self, taskTitle, taskDescription, dueDate, priority):

        self.taskTitle = taskTitle
        self.taskDescription = taskDescription
        self.dueDate = dueDate
        self.priority = priority
        self.complete = False

    #for reference
    #getters
    def get_taskTitle(self):
        return self.taskTitle
    def get_taskDescription(self):
        return self.taskDescription
    def get_priority(self):
        return self.priority
    def get_dueDate(self):
        return self.dueDate
    def get_completeStatus(self):
        return self.complete
    #setters
    def set_taskTitle(self, taskTitle):
        self.taskTitle = taskTitle
    def set_taskDescription(self, taskDescription):
        self.taskDescription = taskDescription
    def set_priority(self, priority):
        self.priority = priority
    def set_dueDate(self, dueDate):
        self.dueDate = dueDate
    def set_completeStatus(self, complete):
        self.complete = complete

    def mark_complete(self):
        self.complete = True

    @property
    def __str__(self):
        return f"{self.taskTitle}: {self.taskDescription} (P{self.priority}) Due:{self.dueDate} {self.complete}"

class Subcategory:
    def __init__(self, subcategoryTitle):
        self.subcategoryTitle = subcategoryTitle
        self.tasks = []

    #management for subcategory
    #getters
    def get_subcategoryTitle(self):
        return self.subcategoryTitle
    def get_tasks(self):
        return self.tasks
    #setters
    def set_subcategoryTitle(self, subcategoryTitle):
        self.subcategoryTitle = subcategoryTitle

    #management for tasks in subcategory
    def add_task(self, Title, Description, dueDate, priority):
        new_task = Task(Title, Description, dueDate, priority)
        self.tasks.append(new_task)
        return new_task
        
    def sort_tasks(self):
        # sorting using lambda allows me to sort by specific keys, and a tuple in this case acts as a key that can hold multiple items
        self.tasks.sort(key=lambda task: (task.dueDate, task.priority))

    def complete_task(self, number): #make sure that we distinguish completed and uncompleted tasks, but not delete completed tasks (so can view completed)
        if 0 <= number < len(self.tasks):
            self.tasks[number-1].mark_complete()
            # print(f"Task #{number}: {self.tasks[number-1].taskTitle()} is complete!") UI
            return True
        return False

    def delete_task(self, number): # make sure that we have the chance to acc remove tasks
        boolean = False
        for index in range(len(self.tasks)):  # iterate through the indicies of the list
            if number - 1 == index:
                boolean = True
                break
        if boolean:
            del self.tasks[number-1]
            #print("Task Deleted!") add to UI
            return True
        return False
            # print("You did not choose an existing task.") UI

class Category:
    def __init__(self, categoryTitle):
        self.categoryTitle = categoryTitle
        self.subcategories = []
        self.tasks = []

    #management for category
    #getters
    def get_categoryTitle(self):
        return self.categoryTitle
    def get_subcategories(self):
        return self.subcategories
    def get_tasks(self):
        return self.tasks
    #setters
    def set_categoryTitle(self, categoryTitle):
        self.categoryTitle = categoryTitle

    #management for tasks in category
    def add_task(self, Title, Description, dueDate, priority):
        new_task = Task(Title, Description, dueDate, priority)
        self.tasks.append(new_task)
        return new_task
        
    def sort_tasks(self):
        #sorting using lambda allows me to sort by specific keys, and a tuple in this case acts as a key that can hold multiple items
        self.tasks.sort(key=lambda task: (task.get_dueDate, task.get_priority))
        
    def complete_task(self, number): #make sure that we distinguish completed and uncompleted tasks, but not delete completed tasks (so can view completed)
        if 0 <= number < len(self.tasks):
            self.tasks[number-1].mark_complete()
            return True
        #print(f"Task #{number}: {self.tasks[number-1].get_taskTitle()} is complete!") add UI
        return False

    def delete_task(self, number): # make sure that we have the chance to acc remove tasks
        boolean = False
        for index in range(len(self.tasks)):  # iterate through the indicies of the list
            if number - 1 == index:
                boolean = True
                break
        if boolean:
            del self.tasks[number-1]
            return True
            #print("Task Deleted!") UI
        return False
            #print("You did not choose an existing task.") UI

    #management for subcategories
    def add_subcategory(self, subcategoryTitle):

        #add in check for duplicate subcategory
        if subcategoryTitle not in self.subcategories:
            new_subcategory = Subcategory(subcategoryTitle)
            self.subcategories.append(new_subcategory)
            return new_subcategory
        #add message if dupe subcat

    #add a find subcategoyr method
    def find_subcategory(self, subcategoryTitle):

        for subcat in self.subcategories:
            if subcat.get_subcategoryTitle() == subcategoryTitle:
                return subcat
        return None

    def view_subcategory_titles(self):
        if not self.subcategories:
            print("No subcategories yet") #ui...
        else:
            for number, subcategories in enumerate(self.subcategories):
                print(f"{number + 1}. {subcategories.get_subcategoryTitle}")
                print()

    def delete_subcategory(self, number):
        boolean = False
        for index in range(len(self.subcategories)):  # iterate through the indicies of the list
            if number - 1 == index:
                boolean = True
                break
        if boolean:
            del self.subcategories[number - 1]
            return True
            #print("Task Deleted!") UI
        return False
            #print("You did not choose an existing task.") UI

    def __str__(self):
        return self.categoryTitle

class TaskManager: # how the tasks will be arranged and managed (prioritization, adding, viewing, deleting etc...)
    def __init__(self):
        self.categories = []
        self.tasks = [] # the list that stores our tasks

    #getters
    def get_categories(self):
        return self.categories
    def get_tasks(self):
        return self.tasks

    #management for tasks outside of both categories
    def add_task(self, Title, Description, dueDate, priority):
        new_task = Task(Title, Description, dueDate, priority)
        self.tasks.append(new_task)
        return new_task

    def sort_tasks(self):
        # sorting using lambda allows me to sort by specific keys, and a tuple in this case acts as a key that can hold multiple items
        self.tasks.sort(key=lambda task: (task.dueDate, task.priority))

    def view_tasks_inTaskManager(self):
        if not self.tasks:
            print("No tasks yet")
        else:
            for number, tasks in enumerate(self.tasks):
                print(f"{number + 1}. {tasks.taskTitle}, P{tasks.priority}")
                print(tasks.taskDescription)
                print()

    def complete_task(self, number): #make sure that we distinguish completed and uncompleted tasks, but not delete completed tasks (so can view completed)
        if 0 <= number < len(self.tasks):
            self.tasks[number-1].mark_complete()
            return True
        return False
        #print(f"Task #{number}: {self.tasks[number-1].get_taskTitle()} is complete!") UI

    def delete_task(self, number): # make sure that we have the chance to acc remove tasks
        boolean = False
        for index in range(len(self.tasks)):  # iterate through the indicies of the list
            if number - 1 == index:
                boolean = True
                break
        if boolean:
            del self.tasks[number-1]
            return True
            #print("Task Deleted!") UI
        return False
            #print("You did not choose an existing task.") UI

    #management for categories

    def add_category(self, categoryTitle):
        #add in check for duplicate categories


        new_category = Category(categoryTitle)
        self.categories.append(new_category)
        return new_category

    def find_category(self, categoryTitle):
        pass

    def view_category_titles(self):
        if not self.categories:
            print("No categories yet")
        else:
            for number, categories in enumerate(self.categories):
                print(f"{number + 1}. {categories.get_categoryTitle}")
                print()

    def delete_category(self, number):
        boolean = False
        for index in range(len(self.categories)):  # iterate through the indicies of the list
            if number - 1 == index:
                boolean = True
                break
        if boolean:
            del self.categories[number - 1]
            return True
            #print("Task Deleted!")
        return False
            #print("You did not choose an existing task.")

    #need to add methods that allow for addition of tasks and subcategories in category, and tasks in subcategory
    def add_subcategory_to_category(self, categoryTitle, subCategoryTitle):

        if categoryTitle in self.categories:
            categoryTitle.add_subcategory(subCategoryTitle)
        else:
            print(f"{categoryTitle} is not a category")


    def add_task_to_category(self, categoryTitle, taskTitle, taskDescription, dueDate, priority):

        if categoryTitle in self.categories:
            categoryTitle.add_task(taskTitle, taskDescription, dueDate, priority)
        else:
            print(f"{categoryTitle} is not a category")
            addCat = input(f"Would you like to add {categoryTitle} as a category? (y/n)")

            if addCat == "y":
                self.add_category(categoryTitle)

    def add_task_to_subcategory(self, categoryTitle, subcategoryTitle, taskTitle, taskDescription, dueDate, priority):

        if categoryTitle in self.categories:
            if subcategoryTitle in categoryTitle.subcategories:
                subcategoryTitle.add_task(taskTitle, taskDescription, dueDate, priority)
            else:
                print(f"{subcategoryTitle} is not a subcategory")
                addSubcat = input(f"Would you like to add {subcategoryTitle} as a subcategory to {categoryTitle}? (y/n)")

                if addSubcat == "y":
                    self.add_subcategory_to_category(categoryTitle, subcategoryTitle)

        else:
            print(f"{categoryTitle} is not a category")
            addCat = input(f"Would you like to add {categoryTitle} as a category? (y/n)")

            if addCat == "y":
                self.add_category(categoryTitle)

    def delete_task_from_category(self, categoryTitle, taskTitle):
        pass
    def delete_task_from_subcategory(self, categoryTitle, subcategoryTitle, taskTitle):
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

