from view.ViewConsole import ViewConsole
from view.TasksListViewConsole import TasksListViewConsole

class TaskManagerViewConsole(TasksListViewConsole, ViewConsole):
    def showActionOptions(self, actionOptions):
        self._reset()
        if any(actionOptions):
            for key,option in actionOptions.items():
                if option:
                    self.print(key, '-', option["message"])
            
    def showTasksList(self, tasksList):
        self._reset()
        self._showTasks(tasksList)
        self._back()
        
    def showActionResponse(self, message):
        self._reset()
        self.print(message)
        self._back()