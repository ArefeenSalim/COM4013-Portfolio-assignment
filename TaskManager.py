tasks_file = "tasks.txt"


def LoadTasks():
    tasks = []
    try:
        with open(tasks_file, "r") as f:
            for line in f:
                name, completed_str = line.strip().split(";", 1)
                tasks.append({"name": name, "completed": completed_str == "True"})
    except:
        pass
    return tasks



def SaveTasks(tasks):
    with open(tasks_file, "w") as f:
        for task in tasks:
            f.write(f"{task['name']};{task['completed']}\n")



def AddTask(tasks):
    name = input("Enter task name: ")
    tasks.append({"name": name, "completed": False})
    print("Task added.")



def ListTasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{i}. {task['name']} - {status}")



def MarkTaskComplete(tasks):
    ListTasks(tasks)
    task_num = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")



def RemoveTask(tasks):
    ListTasks(tasks)
    task_num = int(input("Enter task number to remove: ")) - 1
    if 0 <= task_num < len(tasks):
        removed_task = tasks.pop(task_num)
        print(f"Removed task: {removed_task['name']}")
    else:
        print("Invalid task number.")



def TaskManager():
    tasks = LoadTasks()
    while True:
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
