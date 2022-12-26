from controller.ActionHandler import ActionHandler
from model.TasksList import TasksList
from model.Constants import GET_TASKS_ACTION, ACTION_DB_METHOD, ACTION_REQUEST_DATA

class TaskManager(ActionHandler):
    def __init__(self):
        super().__init__() # <- run the ActionHandler constructor
        self.__tasksList = TasksList(self.performAction(GET_TASKS_ACTION)) # <- instance of TaskList

    
    def performAction(self, action):
        actionMethod = self._actions[action][ACTION_DB_METHOD]
        requestData = self._actions[action][ACTION_REQUEST_DATA]
        data = requestData()
        if data:
            return actionMethod(data)
        else:
            return actionMethod()
    
    def _getTasksList(self):
        self.__tasksList.update(self.performAction(GET_TASKS_ACTION))
        return self.__tasksList