from task import *
from constants import *
import requests


def get_start_command_message():
    start_command_message = requests.get(f"{BASE_URL}/messages").json()["welcome"]
    return start_command_message


def get_books_message():
    books_message = requests.get(f"{BASE_URL}/messages").json()["books"]
    return books_message


def get_help_command_message():
    help_command_message = requests.get(f"{BASE_URL}/messages").json()["help"]
    return help_command_message


def get_about_command_message():
    about_command_message = requests.get(f"{BASE_URL}/messages").json()["about"]
    return about_command_message


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
