from controller.Database import Database
from controller.RequestData import RequestData
from model.Constants import GET_TASKS_ACTION, ADD_TASK_ACTION, EDIT_TASK_ACTION, DELETE_TASK_ACTION
from model.Constants import ACTION_DB_METHOD, ACTION_REQUEST_DATA


class ActionHandler(Database, RequestData):
    def __init__(self):
        super().__init__() # <- run the Database constructor

        self._actions = { # <- dictonary with Database methods
            GET_TASKS_ACTION: {
                ACTION_DB_METHOD: self._getTasks,
                ACTION_REQUEST_DATA: self._requestAmount
            },
            ADD_TASK_ACTION: {
                ACTION_DB_METHOD: self._insertTask,
                ACTION_REQUEST_DATA: self._requestTaskName
            },
            EDIT_TASK_ACTION: {
                ACTION_DB_METHOD: self._editTask,
                ACTION_REQUEST_DATA: self._requestTaskID,
            },
            DELETE_TASK_ACTION: {
                ACTION_DB_METHOD: self._deleteTask,
                ACTION_REQUEST_DATA:  self._requestTaskID
            }
        }
        
        

    