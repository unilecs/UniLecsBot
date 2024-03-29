from core.constants import *
from core.utils import *
import services


info_service = services.InfoService()
task_service = services.TaskService()
puzzle_service = services.PuzzleService()
event_service = services.EventService()


class DataManager:
    @staticmethod
    def get_books(books_type):
        return info_service.get_books_dict()[books_type]

    @staticmethod
    def get_task_list():
        return info_service.get_categories_dict()

    @staticmethod
    def get_test(test):
        return info_service.get_tests_dict()[test]

    @staticmethod
    def get_interview():
        return info_service.get_interview()

    @staticmethod
    def get_past_events():
        events_str = ""
        for event in event_service.get_past_events():
            events_str += get_event_format_text(event)
        return events_str if events_str != "" else EVENT_NOT_FOUND

    @staticmethod
    def get_upcoming_events():
        events_str = ""
        for event in event_service.get_upcoming_events():
            events_str += get_event_format_text(event)
        return events_str if events_str != "" else EVENT_NOT_FOUND

    @staticmethod
    def get_random_task():
        tasks = task_service.get_tasks()
        rnd_task = get_random_item(tasks)
        return get_rnd_task_format_text(rnd_task)

    @staticmethod
    def get_task_by_number(task_num):
        task = get_item_by_number(task_service.get_tasks(), task_num)
        return get_search_task_format_text(task_num, task.announcement_link)

    @staticmethod
    def get_tasks_by_search(search):
        tasks_str = ""
        for task in task_service.get_tasks():
            if task.name.lower().find(search.lower()) != -1:
                tasks_str += get_task_format_text(task)
        return tasks_str

    @staticmethod
    def get_random_puzzle():
        puzzles = puzzle_service.get_puzzles()
        rnd_puzzle = get_random_item(puzzles)
        return get_rnd_puzzle_format_text(rnd_puzzle)
