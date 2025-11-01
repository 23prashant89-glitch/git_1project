import os

TASKS_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from the tasks file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks


def save_tasks(tasks):
    """save tasks to the tasks file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")


def add_task(task):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    return f'Task "{task}" added.'


def remove_tasks(task):
    """Remove a task."""
    tasks = load_tasks()
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
        return f'Task "{task}" removed.'
    else:
        return f'Task "{task}" not found.'


def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        return "No tasks found."
    return "\n".join(f"{idx + 1}. {task}" for idx, task in enumerate(tasks))


def main():
    print("Task Managet CLI")
    print("Command : add <task>, remove <task>, list, exit")

    while True:
        command = input(">>").strip().split(" ", 1)
        action = command[0].lower()

        if action == "add" and len(command) > 1:
            print(add_task(command[1]))
        elif action == "remove" and len(command) > 1:
            print(remove_tasks(command[1]))
        elif action == "list":
            print(list_tasks())
        elif action == "exit":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
