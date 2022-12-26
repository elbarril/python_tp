import datetime

DATABASE_NAME = "database"
DATABASE_TABLE_NAME = "tasks"

ACTION_DB_METHOD = "db_method"
ACTION_REQUEST_DATA = "request_data_method"

APP_TITLE = 'My Tasks'
YEAR = datetime.datetime.now().year

DEFAULT_INPUT = "default"
LIST_TASKS_INPUT = "0"
ADD_TASK_INPUT = "1"
EDIT_TASK_INPUT = "2"
DELETE_TASK_INPUT = "3"
EXIT_INPUT = "7"

DEFAULT_ACTION = "run"
GET_TASKS_ACTION = "get_tasks"
ADD_TASK_ACTION = "add_task"
EDIT_TASK_ACTION = "edit_task"
DELETE_TASK_ACTION = "delete_task"
EXIT_ACTION = "exit"

DEFAULT_OPTION = "run"
LIST_TASKS_OPTION = "list tasks"
ADD_TASK_OPTION = "add_task"
EDIT_TASK_OPTION = "edit_task"
DELETE_TASK_OPTION = "delete_task"
EXIT_OPTION = "exit"

INPUTS = {
    LIST_TASKS_INPUT: {
        "action": GET_TASKS_ACTION,
        "message": LIST_TASKS_OPTION
    },
    ADD_TASK_INPUT: {
        "action": ADD_TASK_ACTION,
        "message": ADD_TASK_OPTION
    },
    EDIT_TASK_INPUT: {
        "action": EDIT_TASK_ACTION,
        "message": EDIT_TASK_OPTION
    },
    DELETE_TASK_INPUT: {
        "action": DELETE_TASK_ACTION,
        "message": DELETE_TASK_OPTION
    },
    EXIT_INPUT: {
        "action": EXIT_ACTION,
        "message": EXIT_OPTION
    },
    DEFAULT_INPUT: False
}

REQUEST_DATA_TEXT = {
    "id": "Enter task ID: ",
    "name": "Enter task name: ",
}