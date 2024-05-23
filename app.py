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

@app.route("/nuevo-usuario")
def formulario_nuevo_usuario():
   return render_template("new-user.html")

@app.route("/crear-usuario")
def crear_usuario():
   cedula = request.args["cedula"]
   nombre=request.args["nombre"]
   apellido=request.args["apellido"]
   usuario_prueba = Usuario( cedula=cedula, nombre=nombre, apellido=apellido, correo="no@tiene.correo", 
                            direccion=request.args["direccion"], telefono=request.args["telefono"], 
                            codigo_departamento=request.args["codigo_departamento"], codigo_municipio=request.args["codigo_municipio"]  ) 
   ControladorUsuarios.Insertar( usuario_prueba )
   return "Aqui se va a crear un usuario"

# Esta linea permite que nuestra aplicación se ejecute individualmente
if __name__=='__main__':
   app.run( debug=True )