from task import *
from constants import *
import requests


def get_books_message():
    books_message = requests.get(f"{BASE_URL}/links").json()["books"]
    return books_message


def get_all_tasks_link():
    books_message = requests.get(f"{BASE_URL}/links").json()["all_tasks"]
    return books_message


def get_categories_dict():
    categories_dict = requests.get(f"{BASE_URL}/categories").json()
    return categories_dict


def get_tasks():
    tasks_from_server = requests.get(f"{BASE_URL}/tasks").json()
    task_list = []

    for task in tasks_from_server:
        task_list.append(
            Task(task["id"],
                 task["name"],
                 task["announcement"],
                 task["solution"],
                 task["complexity"],
                 task["tags"])
        )
    return task_list
