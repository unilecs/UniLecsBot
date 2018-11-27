import sqlite3
from task import Task


class TasksDatabase(object):

    def __init__(self, path: str):

        try:
            self.base_connection = sqlite3.connect(f"file:{path}?mode=rw", uri=True)
        except sqlite3.OperationalError:
            raise OSError("database does not exist")
        else:
            self.base_cursor = self.base_connection.cursor()

    @staticmethod
    def get_sql_response(cursor: sqlite3.Cursor,
                         sql_request: str,
                         arguments: tuple = ()) -> list:
        """
        :param cursor: current database sqlite3 cursor
        :param sql_request: string sql command
        :param arguments: arguments that are passed to the request
        :return: list with responses
        """

        if len(arguments) > 0:
            sql_response = cursor.execute(sql_request, arguments)
        else:
            sql_response = cursor.execute(sql_request)

        return sql_response.fetchall()

    @staticmethod
    def get_tasks(sql_response: list) -> list:
        """
        Create list of Task object
        :param sql_response: list of tuple value from database
        :return: list of task
        """

        if len(sql_response) > 0:
            return [Task(*args) for args in sql_response]
        else:
            return []

    def find_tasks_by_name(self, name: str) -> list:
        """
        Find all tasks with current name substring
        :param name: name substring
        :return: list of tasks
        """

        sql_request = "SELECT * FROM tasks WHERE name LIKE ?"
        sql_response = self.get_sql_response(self.base_cursor,
                                             sql_request,
                                             ('%' + name + '%',)
                                             )

        return self.get_tasks(sql_response)

    def find_task_by_number(self, number: int) -> list:
        """
        Find all tasks with current number
        :param number: task index. Starts with 1
        :return: list of tasks
        """

        sql_request = "SELECT * FROM tasks WHERE number=?"
        sql_response = self.get_sql_response(self.base_cursor,
                                             sql_request,
                                             (int(number),)
                                             )

        return self.get_tasks(sql_response)

    def find_tasks_by_tags(self, tags: list, mode: str = "or") -> list:
        """
        Find all tasks with current tags.
        Mode "or" mean that at least one tag is in the task.
        Mode "and" mean that all tag must be in the task.
        :param tags: list of tags
        :param mode: find mode. Default value "or"
        :return: list of tasks
        """

        if mode.lower() not in ["or", "and"]:
            raise AttributeError(f"mode must be \"or\" or \"and\"")

        logic_separator = ' ' + mode.upper() + ' '
        params_sql_requests = logic_separator.join(['?' for tag in tags])
        base_sql_request = "SELECT * FROM tasks WHERE tags LIKE "

        sql_request = base_sql_request + params_sql_requests
        sql_params = tuple(['%'+param+'%' for param in tags])

        sql_response = self.get_sql_response(self.base_cursor,
                                             sql_request,
                                             sql_params,
                                             )
        return self.get_tasks(sql_response)

    def add_task(self, task: Task):
        """
        Add a new task in database
        :param task: new task object
        :return: None
        """

        max_index = self.base_cursor.execute("SELECT MAX(ind) FROM tasks").fetchone()[0]
        sql_request = f"INSERT INTO tasks VALUES (?, ?, ?)"

        self.base_cursor.execute(
            sql_request,
            (max_index + 1, task.name, task.url,)
        )
        self.base_connection.commit()

    def close(self):
        """
        Close database connection
        :return: None
        """

        self.base_connection.close()
