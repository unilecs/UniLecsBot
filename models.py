from enum import Enum

class SendType(Enum):
    Feedback = 10
    Solution = 20

class Complexity(Enum):
    Easy = 10
    Middle = 20
    Hard = 30

complexityDict = {
    Complexity.Easy: "Легкий",
    Complexity.Middle: "Средний",
    Complexity.Hard: "Тяжелый",
}

class Task(object):
    def __init__(
        self, number, name, announcement_link, solution_link=None, level=None, tags=None
    ):
        self.number = number
        self.name = name
        self.announcement_link = announcement_link
        self.solution_link = solution_link
        self.level = level
        self.tags = tags

    def get_level(self):
        return complexityDict[self.level]

class Puzzle(object):
    def __init__(
        self, number, name, telegram_link, announcement_link, solution_link=None, tags=None
    ):
        self.number = number
        self.name = name
        self.telegram_link = telegram_link
        self.announcement_link = announcement_link
        self.solution_link = solution_link
        self.tags = tags

class Event(object):
    def __init__(
        self, number, name, description, date, link, type, location=None, time=None
    ):
        self.number = number
        self.name = name
        self.description = description
        self.date = date
        self.link = link
        self.type = type
        self.location = location
        self.time = time
