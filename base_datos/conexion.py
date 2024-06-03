import sqlite3


class Conexion:

    def __init__(self, nombre_bd):
        self.conexion = sqlite3.connect(nombre_bd)
        self.cursor = self.conexion.cursor()

    def crear_tabla_usuarios(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS usuarios( nombre TEXT,ciudad TEXT)")
        self.conexion.commit()

    def agregar_usuario(self, nombre, ciudad):
        self.cursor.execute("INSERT INTO usuarios VALUES(?,?)", (nombre,ciudad))

        self.conexion.commit()
    def mostrar_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        clientes = self.cursor.fetchall()
        return clientes
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()