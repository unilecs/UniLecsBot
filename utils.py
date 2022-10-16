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
