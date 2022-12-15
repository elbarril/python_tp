import sqlite3 as sql3
from model.Constants import DATABASE_TABLE_NAME, DATABASE_NAME

class Database:
    def __init__(self):
        self.__connection = self.__connectToDatabase()
        self.__init_database()
        
    def __init_database(self):
        self.__createTable()
    
    def __createTable(self):
        cursor = self.__connection.cursor()
        try:
           cursor.execute(f"""
            CREATE TABLE {DATABASE_TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nameoftask VARCHAR(255),
                status VARCHAR(9)
                )
            """)
        except sql3.OperationalError:
            print("Ya existe la tabla")

    def __connectToDatabase(self):
        return sql3.connect(DATABASE_TABLE_NAME)

    def __closeToDatabase(self):
        self.__connection.close()

    def insertTask(self):
        self.__connection.cursor().execute("INSERT INTO " + DATABASE_TABLE_NAME + "(nameoftask,status) VALUES ('taskname', 'False')")
        self.__connection.commit()

    def modifTask(self):
        self.__connection.cursor().execute("UPDATE " + DATABASE_TABLE_NAME + " SET nameoftask='newtaskname',status='True' WHERE id=3")
        self.__connection.commit()

    def deleteTask(self):
        self.__connection.cursor().execute("DELETE FROM " + DATABASE_TABLE_NAME + " WHERE id=1")

    def getTasks(self):
        return self.__connection.cursor().execute("SELECT * FROM " + DATABASE_TABLE_NAME).fetchall()