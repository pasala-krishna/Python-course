class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Task: {self.name}\nDeadline: {self.deadline}\nStatus: {status}"

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, deadline):
        task = Task(name, deadline)
        self.tasks.append(task)
        print(f"Task '{name}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"Task {i}:\n{task}\n")

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.mark_completed()
            print(f"Task '{task.name}' marked as completed.")
        else:
            print("Invalid task index. Please provide a valid task index.")

# Example usage:
scheduler = TaskScheduler()

scheduler.add_task("Homework", "2023-11-10")
scheduler.add_task("Meeting", "2023-11-15")
scheduler.add_task("Shopping", "2023-11-20")

scheduler.view_tasks()

scheduler.mark_task_completed(2)

scheduler.view_tasks()