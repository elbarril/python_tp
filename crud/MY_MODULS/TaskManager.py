from MY_MODULS.Database import Database

class TaskManager:
    __tasksList = []
    def __init__(self):
        self.__database = Database()
        
    def loadTasks(self):
        self.__tasksList = self.__database.getTasks()
    
    def showTasks(self):
        print(self.__tasksList)

    def getTasks(self):
        return self.__tasksList