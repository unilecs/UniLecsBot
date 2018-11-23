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
    def __init__(self, number, name, announcementLink, solutionlink=None, level=None, tags=None):
        self.number = number
        self.name = name
        self.announcementLink = announcementLink
        self.solutionlink = solutionlink
        self.level = level
        self.tags = tags

    def getLevel(self):
        return complexityDict[self.level]