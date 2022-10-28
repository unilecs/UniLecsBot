import time
from random import randint

def get_task_by_number(tasks, number):
    try:
        return next((x for x in tasks if x.number == number), None)
    except:
        return None


def get_random_task(tasks):
    rand = randint(1, len(tasks))
    if 1 <= rand <= len(tasks):
        return get_task_by_number(tasks, rand)
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
