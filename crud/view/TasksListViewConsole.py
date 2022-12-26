from view.ViewConsole import ViewConsole

class TasksListViewConsole(ViewConsole):
    def _showTasks(self, tasks):
        if any(tasks):
            print("-- Tasks List --")
            
            for task in tasks:
                id = str(task["id"])
                name = task["name"]
                status = "completed" if task["completed"] else "pending"
                print(f"ID {id} - {name} ({status})")
        else:
            print("There is not tasks.")