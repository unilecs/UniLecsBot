import sqlite3
from task import Task, Complexity


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
        :return: list of tasks
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
                                             ('%'+name+'%',)
                                             )

        return self.get_tasks(sql_response)

    def find_task_by_number(self, number: int) -> Task:
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
        try:
            task = self.get_tasks(sql_response)[0]
        except IndexError:
            raise ValueError("task number out of range")
        else:
            return task

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

        logic_separator = ' ' + mode.upper() + " tags LIKE "
        params_sql_request = logic_separator.join(['?' for tag in tags])
        base_sql_request = "SELECT * FROM tasks WHERE tags LIKE "

        sql_request = base_sql_request + params_sql_request
        sql_params = tuple(['%'+param+'%' for param in tags])

        sql_response = self.get_sql_response(self.base_cursor,
                                             sql_request,
                                             sql_params,
                                             )
        return self.get_tasks(sql_response)

    def find_tasks_by_level(self, level: Complexity) -> list:
        """
        Find all tasks with current level
        :param level:
        :return: list of tasks
        """

        if type(level) is not Complexity:
            raise AttributeError(f"type must be enum \"Complexity\"")

        sql_request = "SELECT * FROM tasks WHERE level=?"
        sql_response = self.get_sql_response(self.base_cursor,
                                             sql_request,
                                             (level.value,)
                                             )

        return self.get_tasks(sql_response)

    def add_task(self, task: Task) -> None:
        """
        Add a new task in database
        :param task: new task object
        :return: None
        """

        max_index = self.base_cursor.execute("SELECT MAX(number) FROM tasks").fetchone()[0]
        if max_index > task.number:
            raise ValueError(f"task №{task.number} exist in the database")

        task_values = task.get_values()
        task_values[5] = '|'.join(task_values[5])

        sql_request = "INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?)"
        params_sql_request = tuple(task_values)

        self.base_cursor.execute(sql_request,
                                 params_sql_request
                                 )

    def edit_task(self, number: int, new_values: dict) -> None:
        """
        Change task values in the database
        :param number: task number
        :param new_values: the dictionary where Key is column`s name in the database
        :return: None
        """

        name_of_class_attributes = ["number", "name", "announcement_link",
                                    "solution_link", "level", "tags"]
        column_names = list(new_values.keys())

        for column_name in column_names:
            if column_name not in name_of_class_attributes:
                raise ValueError(f"task has no attribute {column_name}")
            elif type(column_name) is not str:
                raise ValueError(f"column_name {column_name} must be string")

        column_names = [name+"=?" for name in column_names]
        sql_request = "UPDATE tasks SET " + ', '.join(column_names) + " WHERE number=?"
        sql_params = tuple(new_values.values()) + (int(number),)

        self.base_cursor.execute(sql_request, sql_params)

    def close(self, save: bool = True):
        """
        Closing the database connection with/without saving changes
        :param save: True - save changes, False - undo changes
        :return: None
        """

        if save:
            self.base_connection.commit()

        self.base_connection.close()
