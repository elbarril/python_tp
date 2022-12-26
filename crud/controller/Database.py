import sqlite3 as sql3
from model.Constants import DATABASE_TABLE_NAME, DATABASE_NAME

class Database:
    __connection = ""
    
    def __init__(self):
        self.__connect()
        self.__createTable()
        self.__disconnect()
    
    def __createTable(self):
        cursor = self.__connection.cursor()
        try:
           cursor.execute(f"""
            CREATE TABLE {DATABASE_TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255),
                completed BOOLEAN
                )
            """)
        except sql3.OperationalError:
            return "Ya existe la tabla"

    def __connect(self):
        self.__connection = sql3.connect(DATABASE_NAME)

    def __disconnect(self):
        self.__connection.close()

    def _insertTask(self, taskName):
        self.__connect()
        response = ""
        try:
            query = "INSERT INTO " + DATABASE_TABLE_NAME + "(name,completed) VALUES ('" + taskName + "', 0)"
            self.__connection.cursor().execute(query)
            self.__connection.commit()
            response = "Task was added."
        except sql3.Error as error:
            response = f"There was an error. {error}"
        finally:
            self.__disconnect()
            return response

    def _editTask(self, taskID):
        self.__connect()
        response = ""
        try:
            if self._getTask(taskID):
                query = "UPDATE " + DATABASE_TABLE_NAME + " SET completed=1 WHERE id=" + taskID
                self.__connection.cursor().execute(query)
                self.__connection.commit()
                response = "Task was updated."
            else:
                response = f"There is not task with id {taskID}."
        except sql3.Error as error:
            response = f"There was an error. {error}"
        finally:
            self.__disconnect()
            return response

    def _deleteTask(self, taskID):
        self.__connect()
        response = ""
        try:
            if self._getTask(taskID):
                query = "DELETE FROM " + DATABASE_TABLE_NAME + " WHERE id=" + taskID
                self.__connection.cursor().execute(query)
                self.__connection.commit()
                response = "Task was deleted."
            else:
                response = f"There is not task with id {taskID}."
        except sql3.Error as error:
            response = f"There was an error. {error}"
        finally:
            self.__disconnect()
            return response

    def _getTasks(self):
        self.__connect()
        tasks = ""
        query = "SELECT * FROM " + DATABASE_TABLE_NAME
        tasks = self.__connection.cursor().execute(query).fetchall()
        self.__disconnect()
        return tasks
    
    def _getTask(self, taskId):
        self.__connect()
        query = "SELECT * FROM " + DATABASE_TABLE_NAME + " WHERE id=" + taskId
        task = self.__connection.cursor().execute(query).fetchone()
        return task