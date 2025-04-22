todo = []

while True:

    user = input("Press '1' to create a new task, '2' to delete an existing task, '3' to see all tasks, '0' to quit.")
    if user == '1':
        task = input("New task: ")
        todo.append(task)
    if user == '2':
        print(todo)
        delete = int(input("Choose an existing task to delete (1,2,3,... ->): "))
        boolean = False
        for index in range(len(todo)): #1 -> length of list
            print(index)
            if delete == index:
                boolean = True
                break
        if boolean:
            todo.pop(delete-1)
            print("Task Deleted!")
        else:
            print("You did not choose an existing task.")
    if user == '3':
        print(todo)
    if user == '0':
        break


