import sqlite3 as sql3
connection = sql3.connect("databasetasks")
cursor = connection.cursor()
table_name = "opcionesytareas"
from MY_MODULS.TASKS import *
options = tasks["Options"]

def show_options():
    for option_number in range(len(options)): 
        option_of_action_str = str(option_number+1)
        print(option_of_action_str + ".", options[option_number].capitalize())

def ask_for_option():
    chosen_option = input("Enter option: ")

    while not chosen_option or not int(chosen_option) in range(1,len(options)+1):
        chosen_option = input("Enter valid option: ")


    return chosen_option

def show_chosen_option(chosen_option):
    Index_option = int(chosen_option)-1 
    option = options[Index_option]
    print("You choise", option, "\n")

def Execute_option(chosen_option):
    if chosen_option == "1":
        status_task = True if cursor.execute("SELECT id FROM opcionesytareas") == 1 else False
        cursor.execute("SELECT id, nameoftask, status FROM opcionesytareas")
        opcionesytareas = cursor.fetchall()
        for opandtasks in opcionesytareas:
            print(opandtasks)
        connection.commit()
            
    elif chosen_option == "2":
        name_new_task = input("Enter name of task: ")
        new_task = [name_new_task, False]
        list_of_tasks = tasks["list"]
        for id_task in range(len(list_of_tasks)):
            status_task = True if cursor.execute("SELECT id FROM opcionesytareas") == 1 else False
        print(cursor.execute(f"""INSERT INTO opcionesytareas (nameoftask,status) VALUES('{name_new_task}','{status_task}')""").lastrowid)
        last_id = cursor.execute("SELECT id, nameoftask, status FROM opcionesytareas").lastrowid
        option_two = cursor.execute(f"""SELECT id, nameoftask, status FROM opcionesytareas WHERE id={last_id}""")
        print("\n===================\n")
        print("New task")
        opcionesytareas = cursor.fetchall()
        for option_two in opcionesytareas:
            print(option_two)
        connection.commit()
        

    elif chosen_option == "3":
        id_task_to_edit = input("Enter ID of the task to edit: ")
        new_task_name = input("New task name (leave empty to not change):") 
        is_complete = True if input("Complete task? (yes/no): ").lower() == 'yes' else False
        cursor.execute(f"""UPDATE opcionesytareas SET nameoftask='{new_task_name}',status='{is_complete}' WHERE id={id_task_to_edit}""")
        print("\n===================\n") 
        print("Updated task") 
        connection.commit()

        
    elif chosen_option == "4":
        id_task_to_delete = int(input("Enter ID of the task to delete: "))
        cursor.execute(f"""DELETE FROM opcionesytareas WHERE id={id_task_to_delete}""")
        print("\n===================\n")
        print("Updated list")
        connection.commit()

def RUNprogram(initiated = False):
    running = True
    chosen_option = ''
    if not initiated:
        print("\n===== Options =====")
        show_options() 

    print("===================\n") 

    chosen_option = ask_for_option() 
    if chosen_option == "5":
        running = False
    print("\n===================\n")

    show_chosen_option(chosen_option) 

    Execute_option(chosen_option)

    if running:
        RUNprogram(True)

RUNprogram()
print("Has been successfully closed.")