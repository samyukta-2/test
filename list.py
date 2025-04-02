tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

