class Task(object):

    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url


    def show(self):
        return f"*Task {self.name}*\n {self.url}"