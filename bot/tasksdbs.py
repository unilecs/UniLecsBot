import sqlite3


class Task(object):

    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    def show(self):
        return f"*Task {self.name}*\n {self.url}"


class TasksDatabase(object):

    def __init__(self, path: str):

        try:
            self.base_connection = sqlite3.connect(path)
        except sqlite3.DatabaseError:
            print("ERROR! Wrong path")
        finally:
            self.base_cursor = self.base_connection.cursor()


    def find_tasks(self, **kwargs) -> list:
        """
        find all tasks with current index or name substring.
        :param kwargs: index, name
        :return: list of find task
        """

        if len(kwargs) == 0:
            raise AttributeError

        if "index" in kwargs:
            sql_request = f"SELECT name, url FROM tasks WHERE ind = {kwargs['index']}"
        else:
            sql_request = f"SELECT name, url FROM tasks WHERE name LIKE '%{kwargs['name']}%'"

        sql_response = tuple(self.base_cursor.execute(sql_request))

        tasks = []
        if len(sql_response) > 0:
            for (name, url) in sql_response:
                tasks.append(Task(name, url))

        return tasks

    def add_task(self, task: Task):
        """
        Add a new task in database
        :param task: new task object
        :return: None
        """

        max_index = self.base_cursor.execute("SELECT MAX(ind) FROM tasks").fetchone()[0]
        sql_request = f"INSERT INTO tasks VALUES ({max_index+1}, '{task.name}', '{task.url}')"

        self.base_cursor.execute(sql_request)
        self.base_connection.commit()


    def close(self):
        """
        Close database connection
        :return: None
        """

        self.base_connection.close()