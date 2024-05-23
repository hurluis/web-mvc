# Para las aplicaciones web creadas con Flask, debemos importar siempre el modulo flask
# la clase request permite acceso a la información de la petición HTTP
from flask import Flask, request, jsonify , url_for   

# Para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template
from flask import render_template

from src.model.Usuario import Usuario
import src.controller.ControladorUsuarios as ControladorUsuarios

# Flask constructor: crea una variable que nos servirá para comunicarle a Flask
# la configuración que queremos para nuestra aplicación
app = Flask(__name__)     

@app.route("/")
def Home():
   return render_template("index.html")

@app.route("/usuario")
def buscar_usuario():
   # request.args es un diccionario que contiene los parametros en le URL solicitada
   cedula = request.args["cedula"]
   usuario = ControladorUsuarios.BuscarPorCedula(cedula)
   return render_template("usuario.html", user = usuario )

@app.route("/crear-usuario")
def crear_usuario():
   cedula = request.args["cedula"]
   usuario_prueba = Usuario( cedula, "Usuario", "Prueba", "no@tiene.correo", "EN la calle", "99999", "05", "05001"  ) 
   ControladorUsuarios.Insertar( usuario_prueba )
   return "Aqui se va a crear un usuario"

# Esta linea permite que nuestra aplicación se ejecute individualmente
if __name__=='__main__':
   app.run( debug=True )