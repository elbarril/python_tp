from MY_MODULS.TASKS import * # importa todas las tareas seleccionando el archivo luego de la carpeta 

options = tasks["Options"] # options se iguala a la lista de opciones

def show_options(): # funcion para mostrar las opciones
    for option_number in range(len(options)): # loop que itera las pociciones convirtiendo a numero (range) 
        option_of_action_str = str(option_number+1) # se guarda en una variable la option_number como string

        print(option_of_action_str + ".", options[option_number].capitalize()) # mostrar primero el numero de la opcion y despues la oracion (capitalizer = primera letra mayuscula)


# pedir una opción
def ask_for_option():
    chosen_option = input("Enter option: ") # variable igualada a lo que ingresa el usuario

    # si se ingresa un simbolo que no se debería, lo va a volver a pedir
    while not chosen_option or not int(chosen_option) in range(1,len(options)+1):
        chosen_option = input("Enter valid option: ")


    return chosen_option # retornar la opcion para usarla fuera
        
def show_chosen_option(chosen_option):
    Index_option = int(chosen_option)-1 # variable igualada al numero de opcion que se eligio menos -1 para presicion

    option = options[Index_option] # busca en opciones(string) el elemento que está en el index(posicion) que pasó

    print("You choise", option, "\n") # se muestra la opcion y se salta de linea
        


def Execute_option(chosen_option):
    if chosen_option == "1": # si la opcion es 1
        list_of_tasks = tasks["list"] # la variable = a la tupla de las tareas (tupla (), lista[], diccionario{})
        for id_task in range(len(list_of_tasks)): # se define el boucle en que itera cada posicion de la tupla de tareas
            name_task = list_of_tasks[id_task][0] # la variable será el nombre de cada tarea(lista)
            status_task = "(complete)" if list_of_tasks[id_task][1] else "(pending)" # el estado es completo si la id es 1, sino sera pendiente (verdadero = completo, false = pendiente)
            print(str(id_task+1)+".", name_task,  status_task) # mostrar la id (+1 para mostrar correctamente, como string), luego el nombre de la tarea y el estado

    elif chosen_option == "2":
        name_new_task = input("Enter name of task: ") # variable igualada a una nueva tarea con nombre ingresado por comando
        new_task = [name_new_task, False] # se guarda en una nueva variable la nueva tarea que tendra una lista con el nuevo nombre y el estado (pendiente) 
        tasks["list"] = tasks["list"] + [new_task] # ( tasks["list"] = tasks["list"] + (new_task,) es como agregar un elemento en la tupla (tambien sin ()) (se guarda la lista = toda la lista + nuevo elemento) )
        Index_new_tasks = len(tasks["list"]) - 1 # se guarda dentro de la lista, se le resta 1 para ser mas preciso
        print("\n===================\n") #salto de linea
        print("New task") # mostrar
        show_task(tasks["list"][Index_new_tasks]) # mostrar con la funcion en tareas.py pasando el index(indice) de la nueva tarea por parámetro

    elif chosen_option == "3":
        id_task_to_edit = int(input("Enter ID of the task to edit: ")) - 1 # ingresar el id de la tarea a editar, pasado a int y restandole 1
        new_task_name = input("New task name (leave empty to not change):") # nuevo nombre o no dejando vacio en variable
        is_complete = input("Compleer task? (yes/no): ") # variable que pregunta si se completa o no
        tasks["list"][id_task_to_edit][0] = new_task_name if new_task_name else tasks["list"][id_task_to_edit][0] # si el nombre se cambió, se muestra el actual, sino, el que ya estaba guardado
        tasks["list"][id_task_to_edit][1] = True if is_complete.lower() == 'yes' else True if tasks["list"][id_task_to_edit][1] else False # si la respuesta es "si" a completar la tarea, el "false" de tareas.py cambia, sino, se muestra el que estaba(false), y eso sólo si el que estaba era "true", sino poner "false"
        print("\n===================\n") # salto de linea
        print("Updated task") # mostrar
        show_task(tasks["list"][id_task_to_edit]) # mostrar con la funcion en tareas.py pasandola el id de parámetro
        
        
    elif chosen_option == "4":
        id_task_to_delete = int(input("Enter ID of the task to delete: ")) - 1
        deleted_task = tasks["list"][id_task_to_delete]
        tasks["list"].pop(id_task_to_delete)
        print("\n===================\n")
        print("Updated list")
        show_deleted_task(deleted_task)

def RUNprogram(initiated = False): # se define la funcion para correr el programa
    if not initiated: # si no es True
        print("\n===== Options =====")
        show_options() # funcion para mostrar las opciones

    print("===================\n") # salto de linea
    
    chosen_option = ask_for_option() # se llama a la funcion para elegir la opcion
    print("\n===================\n")

    show_chosen_option(chosen_option) # funcion que muestra la opcion elegida

    Execute_option(chosen_option) # funcion para ejecutar la opcion elegida
    
    RUNprogram(True) # cambia el booleano para volver a correr el programa


RUNprogram() # correr el programa nuevamente