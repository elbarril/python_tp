from mis_modulos.tareas import *

opciones = tareas["opciones"]

def mostrar_opciones():
    for opcion in range(len(opciones)): 
        opcion_de_accion_str = str(opcion+1)

        print(opcion_de_accion_str + ". " + opciones[opcion].capitalize())

def solicitar_opcion():
    opcion_elegida = input("Ingresar opción: ")

    while not opcion_elegida or not int(opcion_elegida) in range(1,len(opciones)+1):
        opcion_elegida = input("Ingresar opción válida: ")

    return opcion_elegida
        
def mostrar_opcion_elegida(opcion_elegida):
    indice_opcion = int(opcion_elegida)-1

    opcion = opciones[indice_opcion]

    print("Elegiste", opcion, "\n")
        
def ejecutar_opcion_elegida(opcion_elegida):
    if opcion_elegida == "1":
        lista_de_tareas = tareas["lista"]
        for id_tarea in range(len(tareas["lista"])):
            nombre_tarea = lista_de_tareas[id_tarea][0]
            estado_tarea = "(completada)" if lista_de_tareas[id_tarea][1] else "(pendiente)"
            print(str(id_tarea+1), nombre_tarea,  estado_tarea)

    elif opcion_elegida == "2":
        nombre_nueva_tarea = input("Ingresar nombre de tarea: ")
        nueva_tarea = [nombre_nueva_tarea, False]
        tareas["lista"] = tareas["lista"] + (nueva_tarea,)
        index_nueva_tarea = len(tareas["lista"]) - 1
        print("\n===================\n")
        print("Nueva Tarea")
        mostrar_tarea(tareas["lista"][index_nueva_tarea])

    elif opcion_elegida == "3":
        id_tarea_a_editar = int(input("Ingresar id de tarea a editar: ")) - 1
        nuevo_nombre_de_tarea = input("Nuevo nombre de tarea (dejar vacio para no cambiar):")
        completar = input("Completar tarea? (si/no): ")
        tareas["lista"][id_tarea_a_editar][0] = nuevo_nombre_de_tarea if nuevo_nombre_de_tarea else tareas["lista"][id_tarea_a_editar][0]
        tareas["lista"][id_tarea_a_editar][1] = True if completar.lower() == 'si' else tareas["lista"][id_tarea_a_editar][1] if tareas["lista"][id_tarea_a_editar][1] else False
        print("\n===================\n")
        print("Tarea Actualizada")
        mostrar_tarea(tareas["lista"][id_tarea_a_editar])

def correr_programa(iniciado = False):
    if not iniciado:
        print("\n===== Opciones =====")
        mostrar_opciones()

    print("===================\n")
    
    opcion_elegida = solicitar_opcion()
    print("\n===================\n")

    mostrar_opcion_elegida(opcion_elegida)

    ejecutar_opcion_elegida(opcion_elegida)
    
    correr_programa(True)

correr_programa()