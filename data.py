import os
from task import *
from constants import *
import requests
from requests.structures import CaseInsensitiveDict

JSON_URL = os.environ["JSON_URL"]
JSON_URL_VERSION = os.environ["JSON_URL_VERSION"]
JSON_ACCESS_KEY = os.environ["JSON_ACCESS_KEY"]

headers = CaseInsensitiveDict()
headers["X-ACCESS-KEY"] = JSON_ACCESS_KEY


class DataService:
    def __init__(self, data=None, version=None):
        self.data = data
        self.version = version

    def get_bot_data(self):
        if self.data is None or self.version != JSON_URL_VERSION:
            response = requests.get(JSON_URL, headers=headers)
            self.version = JSON_URL_VERSION
            self.data = (
                response.json()["record"]
                if response and response.status_code == 200
                else None
            )
        return self.data

    def get_books_message(self):
        books_message = self.get_bot_data()["books"]
        return books_message

    def get_all_tasks_link(self):
        books_message = self.get_bot_data()["all_tasks"]
        return books_message

    def get_categories_dict(self):
        categories_dict = self.get_bot_data()["categories"]
        return categories_dict

    def get_tasks(self):
        tasks_from_server = self.get_bot_data()["tasks"]
        task_list = []

        for task in tasks_from_server:
            task_list.append(
                Task(
                    task["id"],
                    task["name"],
                    task["announcement"],
                    task["solution"],
                    task["complexity"],
                    task["tags"],
                )
            )
        return task_list
