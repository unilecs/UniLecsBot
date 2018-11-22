import sqlite3


class TasksDatabase(object):

    def __init__(self, path: str):

        try:
            self.base_connection = self.get_connection(path)
        except sqlite3.DatabaseError:
            print("ERROR! Wrong path")
        finally:
            self.base_cursor = self.get_cursor(self.base_connection)

    @staticmethod
    def get_connection(path: str) -> sqlite3.Connection:
        """
        :param path:
        :return:
        """
        return sqlite3.connect(path)

    @staticmethod
    def get_cursor(connection) -> sqlite3.Cursor:
        """
        :param connection:
        :return:
        """
        return connection.cursor()

    def find_task(self, **kwargs) -> dict:
        """
        :param index:
        :param name:
        :return:
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
            for (task_name, task_url) in sql_response:
                tasks.append(
                    {
                        "task_name": task_name,
                        "task_url": task_url
                    }
                )

        return tasks