import mysql.connector

class DatabaseSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def get_connection(self):
        if self.connection is None or not self.connection.is_connected():
            try:
                self.connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="hotel_mpc"
                )
                print("Conexión exitosa a la base de datos")
            except mysql.connector.Error as e:
                print(f"Error al conectar a la base de datos: {e}")
                self.connection = None  # Reiniciar la conexión a None en caso de error
        return self.connection

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None
