import sqlite3


class Conexion:

    def __init__(self, nombre_bd):
        self.conexion = sqlite3.connect(nombre_bd)
        self.cursor = self.conexion.cursor()

    def crear_tabla_usuarios(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS usuarios( edad TEXT,ciudad TEXT, canilla TEXT,ducha TEXT,manos TEXT,dientes TEXT,platos TEXT,lavarropas TEXT,descarga TEXT,perdidas TEXT,coche TEXT,ropa TEXT,vaca TEXT,pollo TEXT,cerdo TEXT,vereda TEXT,frutas TEXT,verduras TEXT,litros TEXT)")
        self.conexion.commit()

    def agregar_usuario(self, edad,ciudad,canilla,ducha,manos,dientes,platos,lavarropas,descarga,perdidas,coche,ropa,vaca,pollo,cerdo,vereda,frutas,verduras,litros):
        self.cursor.execute("INSERT INTO usuarios VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (edad,ciudad,canilla,ducha,manos,dientes,platos,lavarropas,descarga,perdidas,coche,ropa,vaca,pollo,cerdo,vereda,frutas,verduras,litros))

        self.conexion.commit()
    def mostrar_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        clientes = self.cursor.fetchall()
        return clientes
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()