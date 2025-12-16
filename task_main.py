from task_manager_class import TaskManager, task_logger
from task_utils import format_result, simple_calculation

# task functions which will be logged

@task_logger
def send_reminder(name):
    return f"Reminder sent to {name}"

@task_logger
def create_report():
    return "Report generated successfully"

@task_logger
def add_two_numbers(x, y):
    return x + y

# main execution
if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task(send_reminder, "Alice")
    manager.add_task(create_report)
    manager.add_task(add_two_numbers, 10, 20)

    manager.run_tasks()

    print("Tasks Added:", manager.view_tasks())
