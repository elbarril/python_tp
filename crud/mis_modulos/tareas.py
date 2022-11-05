tasks = {
    "opciones":[
        "listar tareas",
        "crear tarea",
        "editar tarea",
        "borrar tarea"
    ],
    "lista": (["tarea 1", False],["tarea 2", False],["tarea 3", False])
}

def show_task(task):
    print("Nombre:", task[0]) # mostrar el nombre de la tarea (en "lista" es el string, primera posicion)
    print("Estado:", "Completada" if task[1] else "Pendiente") # mostrar el estado de la tarea, completa si 