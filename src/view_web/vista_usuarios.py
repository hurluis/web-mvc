from flask import Blueprint, render_template, request

blueprint = Blueprint( "vista_usuarios", __name__, "templates" )

import sys
sys.path.append("src")
from model.Usuario import Usuario
import controller.ControladorUsuarios as ControladorUsuarios

@blueprint.route("/")
def Home():
   return render_template("index.html")

@blueprint.route( "/new-user" )
def nuevo():
   return render_template("crear-usuario.html")

@blueprint.route( "/crear-usuario")
def crear_usuario():
   usuario = Usuario( cedula=request.args["cedula"], apellido=request.args["apellido"], nombre=request.args["nombre"], correo=request.args["correo"], direccion=request.args["direccion"], telefono=request.args["telefono"], codigo_departamento=request.args["codigo_departamento"], codigo_municipio=request.args["codigo_municipio"] ) 
   ControladorUsuarios.Insertar( usuario )

   return render_template("usuario.html", user = usuario, mensaje = "Usuario insertado exitosamente!" )

@blueprint.route("/usuario")
def buscar_usuario():
   # request.args es un diccionario que contiene los parametros en le URL solicitada
   cedula = request.args["cedula"]
   usuario = ControladorUsuarios.BuscarPorCedula(cedula)
   return render_template("usuario.html", user = usuario )
