# this is a task manager which allows user to add, list, mark as completed, and remove tasks.


tasks_file = "tasks.txt"


def LoadTasks(): # loads task from tasks.txt file into this python file(TaskManager.py)
    tasks = []
    try: # this loop iterates over each line in the file and splits the line into a task name and a completion status.
        with open(tasks_file, "r") as f: # this loop is important for processing multiple tasks stored in the file converting them into a list of dictionaries
            for line in f:
                name, completed_str = line.strip().split(";", 1)
                tasks.append({"name": name, "completed": completed_str == "True"})
    except:
        pass
    return tasks



def SaveTasks(tasks): # saves the current list of tasks back to the file
    with open(tasks_file, "w") as f: # iterates over each task in the list of tasks.For each task, it writes a line to the file with the task name and completion status. This loop is necessary to ensure all tasks are written back to the file.
        for task in tasks:
            f.write(f"{task['name']};{task['completed']}\n")



def AddTask(tasks): # adds a new task to the list of tasks
    name = input("Enter task name: ")
    tasks.append({"name": name, "completed": False}) # it appends a single new task to the list
    print("Task added.")



def ListTasks(tasks): # lists all tasks to the console, showing their number, name, and completion status
    if not tasks:
        print("No tasks.")
        return
    for i, task in enumerate(tasks, start=1): # iterates over the tasks enumerating them starting from 1.
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{i}. {task['name']} - {status}")
        # the enumeration is very crucial for displaying all the tasks in the list and is useful for selection operations



def MarkTaskComplete(tasks): # marks a specified task as completed
    ListTasks(tasks) # calls ListTasks() which uses a loop to list tasks and directly accesses a task by its index.
    task_num = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")



def RemoveTask(tasks): # removes a task from the list based on the user's input.
    ListTasks(tasks) # calls ListTasks() which uses a loop to list tasks and removes a task based on its index.
    task_num = int(input("Enter task number to remove: ")) - 1
    if 0 <= task_num < len(tasks):
        removed_task = tasks.pop(task_num)
        print(f"Removed task: {removed_task['name']}")
    else:
        print("Invalid task number.")



def TaskManager(): #main function of the program, presenting a menu to the user and handling their input to perform various task management operations
    tasks = LoadTasks()
    while True: # this loop allows the user to repeatedly perform different actions until they choose to exit.
        print("Task Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task Complete") 
        print("4. Remove Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            AddTask(tasks)
        elif choice == "2":
            ListTasks(tasks)
        elif choice == "3":
            MarkTaskComplete(tasks)
        elif choice == "4":
            RemoveTask(tasks)
        elif choice == "5":
            SaveTasks(tasks)
            print("byebye!")
            break
        else:
            print("Invalid choice. Please try again.")
TaskManager()
