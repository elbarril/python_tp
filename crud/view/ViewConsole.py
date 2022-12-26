import os
from model.Constants import APP_TITLE, YEAR

class ViewConsole:
    def _reset(self):
        self._clear()
        self._showTitle()
    
    def _clear(self):
        os.system('cls')
            
    def _showTitle(self):
        print(f"{APP_TITLE} - {YEAR}")
        
    def _back(self):
        input("Enter to continue..")
        self._reset()
        
    def print(self, *data):
        message = ""
        for d in data:
            message += d
        print(message)