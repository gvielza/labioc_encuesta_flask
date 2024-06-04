from flask import Flask, render_template, request

from base_datos.conexion import Conexion

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


def litros_agua_por_anno(canilla, ducha, manos, dientes, platos, lavarropas, descarga, perdidas, coche,vereda, ropa, vaca,
                         pollo, cerdo,frutas,verduras):
    cantidad=0
    if(canilla=="foto1"):
        cantidad=int(ducha)*5475+int(manos)*16425 #27375
    else:
        cantidad=int(ducha)*2737+int(manos)*8212
    if(dientes=="si" and canilla=="foto1"):
        cantidad=cantidad+10950
    if(dientes=="no" and canilla=="foto1"):
        cantidad=cantidad+32850
    if(dientes=="si" and canilla=="foto2"):
        cantidad=cantidad+5475
    if(dientes=="no" and canilla=="foto2"):
        cantidad=cantidad+16425
    if(platos=="1" and canilla=="foto1"):
        cantidad=cantidad+54750
    if(platos=="1" and canilla=="foto2"):
        cantidad=cantidad+27375
    if(platos=="2" and canilla=="foto1"):
        cantidad=cantidad+164250
    if(platos=="2" and canilla=="foto2"):
        cantidad=cantidad+82125
    if(platos=="3"):
        cantidad=cantidad+5475
    cantidad=cantidad+int(lavarropas)*2346
    if(descarga=="si"):
        cantidad=cantidad+4380
    else:
        cantidad=cantidad+7665
    if(perdidas=="si"):
        cantidad=cantidad+1577
    cantidad=cantidad+int(coche)*1200
    if(vereda=="1"):
        cantidad=cantidad+11700
    if(vereda=="2"):
        cantidad=cantidad+3900
    if(vereda=="3"):
        cantidad=cantidad+100
    cantidad=cantidad+int(ropa)*2700
    cantidad=cantidad+int(vaca)*806000
    cantidad=cantidad+int(pollo)*182000
    cantidad=cantidad+int(cerdo)*249600+int(frutas)*31200+int(verduras)*15600


    return cantidad


def mensaje_por_consumo(litros):
    consumo_mundial=1240000
    litros_x_acuario=500
    acuarios=int(litros)/litros_x_acuario

    if(consumo_mundial-litros<50000 and consumo_mundial-litros>0):
        return "Buen trabajo!Tu consumo de agua es similar al promedio mundial. Pequeños cambios pueden hacer una gran diferencia."
    if(consumo_mundial<litros):
        return f"¡Wow! Con tu consumo podrías llenar  {acuarios} acuarios!"
    if(consumo_mundial>litros):
        return  "Impresionante!Tu consumo es menor que el promedio mundial. Sigue así para ayudar a conservar nuestros recursos."



@app.route('/resultados', methods=['POST'])
def resultados():
    nombre = request.form['nombre']
    edad= request.form['edad']
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
    vereda= request.form['vereda']
    frutas= request.form['frutas']
    verduras= request.form['verduras']
    litros = litros_agua_por_anno(canilla, ducha, manos, dientes, platos, lavarropas, descarga, perdidas, coche, vereda,
                                  ropa, vaca, pollo, cerdo, frutas, verduras)
    conexion = Conexion("base_datos/usuarios.db")
    conexion.crear_tabla_usuarios()
    conexion.agregar_usuario(edad, ciudad, canilla, ducha, manos, dientes, platos, lavarropas, descarga, perdidas, coche, ropa, vaca, pollo, cerdo, vereda, frutas, verduras,litros)
    #usuarios=conexion.mostrar_usuarios()

    litros_f=f"{litros:,}".replace(",", ".")
    mensaje=mensaje_por_consumo(litros)
    if(litros>1240000):
        imagen="triste.avif"
    else:
        imagen="feliz.jpg"

    print(litros_f)
    conexion.cerrar_conexion()
    return render_template('resultados.html', nombre=nombre, litros_f=litros_f, mensaje=mensaje,imagen=imagen)



if __name__ == '__main__':
    app.run()
