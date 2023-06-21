import datetime

TASKS_FILE = "tasks.txt"

tasks = []

class Task:
    def __init__(self, title, due_date, priority):
        self.title = title
        self.due_date = due_date
        self.priority = priority

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task.title},{task.due_date},{task.priority}\n")
    print("Tasks saved successfully!")

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            for line in file:
                title, due_date, priority = line.strip().split(",")
                task = Task(title, due_date, int(priority))
                tasks.append(task)
        print("Tasks loaded successfully!")
    except FileNotFoundError:
        print("No tasks found. Starting with an empty task list.")

def create_task():
    title = input("Enter task title: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = int(input("Enter priority level (1-5): "))
    task = Task(title, due_date, priority)
    tasks.append(task)
    print("Task created successfully!")
    save_tasks()

def display_tasks():
    if not tasks:
        print("No tasks found.")
        return

    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.title} - Due: {task.due_date} - Priority: {task.priority}")

def update_task():
    display_tasks()
    task_index = int(input("Enter task number to update: ")) - 1

    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        return

    task = tasks[task_index]

    new_title = input("Enter new task title (leave blank to keep current): ")
    new_due_date = input("Enter new due date (YYYY-MM-DD) (leave blank to keep current): ")
    new_priority = input("Enter new priority level (1-5) (leave blank to keep current): ")

    if new_title:
        task.title = new_title
    if new_due_date:
        task.due_date = new_due_date
    if new_priority:
        task.priority = int(new_priority)

    print("Task updated successfully!")
    save_tasks()

def delete_task():
    display_tasks()
    task_index = int(input("Enter task number to delete: ")) - 1

    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        return

    tasks.pop(task_index)
    print("Task deleted successfully!")
    save_tasks()

def display_menu():
    print("1. Create Task")
    print("2. Display Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Quit")

# Load tasks from file when the program starts
load_tasks()

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        create_task()
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")
