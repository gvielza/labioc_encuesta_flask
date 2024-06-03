from flask import Flask, render_template, request

from base_datos.conexion import Conexion

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/resultados', methods=['POST'])
def resultados():
    nombre = request.form['nombre']
    ciudad = request.form['ciudad']
    canilla = request.form['canilla']
    ducha = request.form['ducha']
    manos= request.form['manos']
    dientes= request.form['dientes']
    platos= request.form['platos']
    lavarropas= request.form['lavarropas']
    descarga= request.form['descarga']
    perdidas= request.form['perdidas']
    coche= request.form['coche']
    ropa= request.form['ropa']
    vaca= request.form['vaca']
    pollo= request.form['pollo']
    cerdo= request.form['cerdo']




    conexion = Conexion("base_datos/usuarios.db")
    conexion.crear_tabla_cliente()
    #conexion.agregar_cliente(dni,usuario,contrasenna)
    clientes = conexion.mostrar_clientes()
    conexion.cerrar_conexion()
    return render_template('resultados.html', nombre=nombre,ciudad=ciudad,canilla=canilla,
                           ducha=ducha
                           ,manos=manos,dientes=dientes,platos=platos,lavarropas=lavarropas,descarga=descarga,
                           perdidas=perdidas,coche=coche,ropa=ropa,vaca=vaca,pollo=pollo,cerdo=cerdo)

@app.route('/nombre_provincia',methods=['GET'])
def nombre_provincia():
    return render_template('nombre_provincia.html')
@app.route('/nombre1', methods=['POST'])
def nombre1():
    nombre1=request.form['nombre1']
    return render_template('index.html', nombre1=nombre1)

if __name__ == '__main__':
    app.run()
