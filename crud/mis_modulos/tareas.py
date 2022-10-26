tareas = {
    "opciones":[
        "listar tareas",
        "crear tarea",
        "editar tarea",
        "borrar tarea"
    ],
    "lista": (["tarea 1", False],["tarea 2", False],["tarea 3", False])
}

def mostrar_tarea(tarea):
    print("Nombre:", tarea[0])
    print("Estado:", "Completada" if tarea[1] else "Pendiente")