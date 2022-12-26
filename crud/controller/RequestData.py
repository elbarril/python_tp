from model.Constants import REQUEST_DATA_TEXT
from view.ViewConsole import ViewConsole

class RequestData(ViewConsole):
    def _requestAmount(self):
        pass

    def _requestTaskName(self):
        self._reset()
        return input(REQUEST_DATA_TEXT["name"])

    def _requestTaskID(self):
        self._reset()
        return input(REQUEST_DATA_TEXT["id"])