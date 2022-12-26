class TasksList():
    __tasks = []

    def __init__(self, tasks):
        self.update(tasks)

    def update(self, tasksList):
        self.__tasks.clear()
        for taskItem in tasksList:
            id, name, completed = taskItem
            self.__tasks.append({"id": id, "name": name, "completed": completed})
    
    def __iter__(self):
        self.__current_index = 0
        return self
    
    def __next__(self):
        if self.__current_index < len(self.__tasks):
            task = self.__tasks[self.__current_index]
            self.__current_index += 1
            return task
        
        raise StopIteration