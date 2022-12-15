from model.TaskManager import TaskManager
from view.TaskManagerViewConsole import TaskManagerViewConsole

class Controller:
    def __init__(self):
        self.__taskManager = TaskManager()
        self.__taskManagerViewConsole = TaskManagerViewConsole()

    def loadTasks(self):
        self.__taskManager.loadTasks()

    def showTasks(self):
        self.__taskManagerViewConsole.showTasks(self.__taskManager.getTasks())

    def addTask(self):
        self.__taskManager.addTask()

    def modifTask (self):
        self.__taskManager.modifTask()

    def deleteTask(self):
        self.__taskManager.deleteTask()