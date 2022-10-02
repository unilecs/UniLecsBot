from enum import Enum


class Complexity(Enum):
    Easy = 10
    Middle = 20
    Hard = 30


complexityDict = {
    Complexity.Easy: 'Легкий',
    Complexity.Middle: 'Средний',
    Complexity.Hard: 'Тяжелый'
}


class Task(object):
    def __init__(self, number, name, announcement_link, solution_link=None, level=None, tags=None):
        self.number = number
        self.name = name
        self.announcement_link = announcement_link
        self.solution_link = solution_link
        self.level = level
        self.tags = tags

    def get_level(self):
        return complexityDict[self.level]
