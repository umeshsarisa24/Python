import os

TODO_FILE = 'todo.txt'

def add_task(task):
    with open(TODO_FILE, 'a') as f:
        f.write(task + '\n')
    print("Task added!")

def view_tasks():
    if not os.path.exists(TODO_FILE):
        print("No tasks yet!")
        return
    with open(TODO_FILE, 'r') as f:
        tasks = f.readlines()
    print("Your tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.strip()}")

def main():
    while True:
        choice = input("Choose: [1] Add Task, [2] View Tasks, [3] Exit: ")
        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
