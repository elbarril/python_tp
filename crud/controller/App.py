from model.Constants import INPUTS, DEFAULT_INPUT, EXIT_INPUT, LIST_TASKS_INPUT
from view.TaskManagerViewConsole import TaskManagerViewConsole
from controller.TaskManager import TaskManager

class App:
    def __init__(self):
        self.__TM = TaskManager()
        self.__TMView = TaskManagerViewConsole()
        self.__action_input = DEFAULT_INPUT

    def run(self):
        self.__TMView.showActionOptions(INPUTS)
        while self.__action_input is not EXIT_INPUT:
            if self.__action_input in INPUTS.keys():
                if self.__action_input is not DEFAULT_INPUT:
                    if self.__action_input is LIST_TASKS_INPUT:
                        self.__TMView.showTasksList(self.__TM._getTasksList())
                    else:
                        actionResponse = self.__TM.performAction(INPUTS[self.__action_input]["action"])
                        if actionResponse:
                            self.__TMView.showActionResponse(actionResponse)
            self.__TMView.showActionOptions(INPUTS)
            self.__action_input = input()
        self.__TMView._clear()