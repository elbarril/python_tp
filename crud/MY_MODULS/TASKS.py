tasks = { # se define la variable (diccionario) "tasks"
    "Options":[ # se define el atributo (lista) "opciones"
        "list tasks",
        "create task",
        "edit task",
        "delete task"
    ],
    "list": [["task 1", False],["task 2", False],["task 3", False]] # se define el atributo (tupla) "lista" con las primeras tareas (listas)
}

def show_task(task):
    print("Name:", task[0]) # mostrar el nombre de la tarea (en "lista" es el string, primera posicion)
    print("Status:", "Complete" if task[1] else "Pending") # mostrar el estado de la tarea, completa si 

def show_deleted_task(task):
    print("Deleted task name:", task[0])
    print("Deleted task status:", "Complete" if task[1] else "Pending")