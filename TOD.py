class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            print("\nTodo List:")
            for index, task in enumerate(self.tasks, 1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{index}. {task['task']} - {status}")

    def mark_completed(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
        else:
            print("Invalid task number.")

    def delete_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks.pop(task_index - 1)
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added successfully.")

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            todo_list.view_tasks()
            task_index = int(input("Enter task number to mark as completed: "))
            todo_list.mark_completed(task_index)

        elif choice == '4':
            todo_list.view_tasks()
            task_index = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_index)

        elif choice == '5':
            print("Exiting Todo List application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            print("\nTodo List:")
            for index, task in enumerate(self.tasks, 1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{index}. {task['task']} - {status}")

    def mark_completed(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks.pop(task_index - 1)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task['task']} - {task['completed']}\n")
        print("Tasks saved successfully.")

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file.readlines():
                    task, completed = line.strip().split(' - ')
                    self.tasks.append({"task": task, "completed": completed == "True"})
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("File not found.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            todo_list.view_tasks()
            task_index = int(input("Enter task number to mark as completed: "))
            todo_list.mark_completed(task_index)

        elif choice == '4':
            todo_list.view_tasks()
            task_index = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_index)

        elif choice == '5':
            filename = input("Enter filename to save tasks: ")
            todo_list.save_tasks(filename)

        elif choice == '6':
            filename = input("Enter filename to load tasks: ")
            todo_list.load_tasks(filename)

        elif choice == '7':
            print("Exiting Todo List application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
       
    