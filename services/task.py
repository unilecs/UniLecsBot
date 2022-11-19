from config import TASKS_URL, TASKS_URL_VERSION, DATA_ACCESS_KEY
from core.models import Task

from requests.structures import CaseInsensitiveDict
import requests

headers = CaseInsensitiveDict()
headers["X-ACCESS-KEY"] = DATA_ACCESS_KEY


class TaskService:
    def __init__(self, data=None, version=None):
        self.data = data
        self.version = version

    def get_task_data(self):
        if self.data is None or self.version != TASKS_URL_VERSION:
            response = requests.get(TASKS_URL, headers=headers)
            self.version = TASKS_URL_VERSION
            self.data = (
                response.json()["record"]
                if response and response.status_code == 200
                else None
            )
        return self.data

    def get_tasks(self):
        tasks_from_server = self.get_task_data()["tasks"]
        task_list = []

        for task in tasks_from_server:
            task_list.append(
                Task(
                    task.get("id", None),
                    task.get("name", None),
                    task.get("announcement", None),
                    task.get("solution", None),
                    task.get("complexity", None),
                    task.get("tags", None),
                )
            )
        return task_list
