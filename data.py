import os
from task import *
from constants import *
import requests
from requests.structures import CaseInsensitiveDict

JSON_URL = os.environ["JSON_URL"]
JSON_ACCESS_KEY = os.environ["JSON_ACCESS_KEY"]

headers = CaseInsensitiveDict()
headers["X-ACCESS-KEY"] = JSON_ACCESS_KEY

bot_data = None

def get_bot_data():
    if bot_data:
        return bot_data
    response = requests.get(JSON_URL, headers=headers)
    bot_data = response.json()["record"] if response and response.status_code == 200 else None

def get_books_message():
    books_message = get_bot_data()["books"]
    return books_message


def get_all_tasks_link():
    books_message = get_bot_data()["all_tasks"]
    return books_message


def get_categories_dict():
    categories_dict = get_bot_data()["categories"]
    return categories_dict


def get_tasks():
    tasks_from_server = get_bot_data()["tasks"]
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
