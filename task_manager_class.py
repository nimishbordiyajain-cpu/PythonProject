import time
from datetime import datetime

# Decorator to log tasks
def task_logger(func):
    def wrapper(*args, **kwargs):
        task_name = func.__name__
        start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"\nExecuting Task: {task_name}")
        print(f"{task_name} - Started")

        # Log start
        with open("task_log.txt", "a") as log:
            log.write(f"{start} - Task: {task_name} - Started\n")

        try:
            result = func(*args, **kwargs)

            end = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{task_name} - Completed - Result: {result}")

            # Log end
            with open("task_log.txt", "a") as log:
                log.write(f"{end} - Task: {task_name} - Completed - Result: {result}\n")

            return result

        except Exception as e:
            print(f"{task_name} - FAILED - Error: {e}")

            with open("task_log.txt", "a") as log:
                log.write(f"{datetime.now()} - Task: {task_name} - FAILED - Error: {e}\n")

    return wrapper


# Task Manager Class
class TaskManager:
    def __init__(self):
        self.tasks = []  # list of tasks

    def add_task(self, func, *args, **kwargs):
        self.tasks.append((func, args, kwargs))

    def run_tasks(self):
        print("\n--- Running All Tasks ---\n")
        for func, args, kwargs in self.tasks:
            func(*args, **kwargs)
            time.sleep(1)

    def view_tasks(self):
        return [task[0].__name__ for task in self.tasks]
