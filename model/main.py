import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Service.Task_service import Task_Service


from Service.User_service import User_Service


def main():
    task_service = Task_Service()
    user_service = User_Service()

    user_service.add_user(1,"pruthviraj","pruthvi@1281.com")

    task_service.create_task(2,"Teach Data struchere basice","Screatch")

    task_service.create_task(3,"Teach Data Science basice","Screatch")

    task_service.create_task(4," Do a project","Screatch")

    print(task_service.complete_task())
    print(task_service.complete_task())
    print(task_service.complete_task())
    print(task_service.complete_task())

    # Print completed task titles from history
    history = task_service.get_task()
    while not history.is_empty():
        print(history.pop().title)

if __name__ == "__main__":
    print("Task_service module is running!")




