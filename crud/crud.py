from mis_modulos.tareas import * # importa todas las tareas seleccionando el archivo luego de la carpeta

options = tasks["opciones"] # options se iguala a la lista de opciones

def show_options(): # funcion para mostrar las opciones
    for option in range(len(options)): # para la opcion dentro de la longitud de la lista de opciones
        option_of_action_str = str(option+1) # la variable es string y se iguala a la opcion (ej; "editar tarea")

        print(option_of_action_str + ". " + options[option].capitalize()) # mostrar primero el numero de la opcion
                                                                          # y despues la oracion

# pedir una opción
def ask_for_option():
    chosen_option = input("Ingresar opción: ") # variable igualada a lo que se ingresa

    # si se ingresa un simbolo que no se debería, lo va a volver a pedir
    while not chosen_option or not int(chosen_option) in range(1,len(options)+1):
        chosen_option = input("Ingresar opción válida: ")


    return chosen_option # retornar la opcion para usarla fuera
        
def show_chosen_option(chosen_option):
    INoption = int(chosen_option)-1 # variable igualada al numero de opcion que se eligio menos -1 para presicion

    option = options[INoption] # option es = a la lista de las opciones dependiento de la opcion introducida

    print("Elegiste", option, "\n") # se muestra la opcion y se salta de linea
        


def EX_option(chosen_option):
    if chosen_option == "1": # si la opcion es 1
        list_of_tasks = tasks["lista"] # variable = a la lista+tupla de las tareas
        for id_task in range(len(tasks["lista"])): # para la id de los tasks en la cantidad de objetos dentro de la tupla de la lista
            name_task = list_of_tasks[id_task][0] # la variable será el nombre de cada objeto
            status_task = "(completada)" if list_of_tasks[id_task][1] else "(pendiente)" # el estado es completo si la id es 1, sino sera pendiente
            print(str(id_task+1), name_task,  status_task) # mostrar la id (+1 para mostrar correctamente), luego el nombre de la tarea y el estado, todo como string

    elif chosen_option == "2":
        name_new_task = input("Ingresar nombre de tarea: ") # colocar una nueva tarea con nombre
        new_task = [name_new_task, False] # la nueva tarea tendra una tupla con el nuevo nombre y el estado (pendiente)
        tasks["lista"] = tasks["lista"] + (new_task,) # como agregar un elemento en la lista
        IN_new_tasks = len(new_task["lista"]) - 1 
        print("\n===================\n") #salto de linea
        print("Nueva Tarea") # mostrar
        show_task(tasks["lista"][IN_new_tasks]) # mostrar con la funcion en tareas.py pasando el index(indice) de la nueva tarea por parámetro

    elif chosen_option == "3":
        id_task_to_edit = int(input("Ingresar id de tarea a editar: ")) - 1 # ingresar el id de la tarea a editar, pasado a int y restandole 1
        name_new_task = input("Nuevo nombre de tarea (dejar vacio para no cambiar):") # nuevo nombre o no dejando vacio
        complete = input("Completar tarea? (si/no): ") # preguntar si se completa o no
        tasks["lista"][id_task_to_edit][0] = name_new_task if name_new_task else tasks["lista"][id_task_to_edit][0] # si el nombre se cambió, se muestra el actual, sino, el que ya estaba
        tasks["lista"][id_task_to_edit][1] = True if complete.lower() == 'si' else tasks["lista"][id_task_to_edit][1] if tasks["lista"][id_task_to_edit][1] else False # si la respuesta es "si" a completar la tarea, el "false" de tareas.py cambia, sino, se muestra el que estaba(false), y eso sólo si el que estaba era "true", sino poner "false"
        print("\n===================\n") # salto de linea
        print("Tarea Actualizada") # mostrar
        show_task(tasks["lista"][id_task_to_edit]) # mostrar con la funcion en tareas.py pasandola el id de parámetro
        
        
    elif chosen_option == "4":
        id_task_to_delete = int(input("Ingresar id de tarea a borrar: ")) - 1
        complete = input("Segurx? (si/no): ")
        tasks["lista"][id_task_to_delete][0] = nuevo_nombre_de_tarea if nuevo_nombre_de_tarea else tasks["lista"][id_task_to_delete][0]
        tasks["lista"][id_task_to_delete][1] = True if complete.lower() == 'si' else tasks["lista"][id_task_to_delete][1] if tasks["lista"][id_task_to_delete][1] else False
        print("\n===================\n")
        print("Lista Actualizada")
        show_task(tasks["lista"][id_task_to_delete])

def RUNprogram(initiated = False):
    if not initiated:
        print("\n===== Opciones =====")
        show_options() # funcion para mostrar las opciones

    print("===================\n") # salto de linea
    
    chosen_option = ask_for_option() # funcio para elegir la opcion
    print("\n===================\n")

    show_chosen_option(chosen_option) # funcion que muestra la opcion elegida

    EX_option(chosen_option) # funcion para modificar con la opcion
    
    RUNprogram(True) # cambia el booleano

RUNprogram() # correr el programa nuevamente