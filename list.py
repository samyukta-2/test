tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option: ")
