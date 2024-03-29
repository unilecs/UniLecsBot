from core.constants import RANDOM_TASK, RANDOM_PUZZLE, EVENT_FORMAT

import time
from datetime import datetime
from random import randint


def get_item_by_number(items, number):
    try:
        return next((x for x in items if x.number == number), None)
    except:
        return None


def get_random_item(items):
    rand = randint(1, len(items))
    if 1 <= rand <= len(items):
        return get_item_by_number(items, rand)
    else:
        return None


def get_feedback_form(message):
    time_at_now = time.strftime("%H:%M:%S %Y.%m.%d", time.localtime())
    form = """Feedback from {0} - @{1} ({2});\nDate: {3};\nText: {4}""".format(
        message.from_user.first_name,
        message.from_user.username,
        message.from_user.id,
        time_at_now,
        message.text,
    )
    return form


def get_task_format_text(task):
    return "*Task {0}: {1}*\n{2}\n\n".format(task.number, task.name, task.announcement_link)


def get_search_task_format_text(text, link):
    return "*Task {0}*\n {1}".format(text, link)


def get_rnd_task_format_text(task):
    return RANDOM_TASK.format(task.number, task.name, task.announcement_link)


def get_rnd_puzzle_format_text(puzzle):
    return RANDOM_PUZZLE.format(puzzle.number, puzzle.name, puzzle.telegram_link)


def get_event_format_text(event):
    event_date = datetime.strptime(event.date, "%d-%m-%Y")
    format_date = event_date.strftime("%d %b %Y")
    return EVENT_FORMAT.format(format_date, event.location, event.name, event.description, event.type, event.link)
