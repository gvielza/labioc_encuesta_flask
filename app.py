from flask import Flask, render_template, request

from base_datos.conexion import Conexion

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultados', methods=['POST'])
def saludo():
    dni = request.form['dni']
    usuario=request.form['usuario']
    contrasenna=request.form['contrasenna']
    conexion=Conexion("base_datos/usuarios.db")
    conexion.crear_tabla_cliente()
    conexion.agregar_cliente(dni,usuario,contrasenna)
    clientes=conexion.mostrar_clientes()
    conexion.cerrar_conexion()
    return render_template('resultados.html', dni=dni, usuario=usuario,clientes=clientes)