import Json
import getpass
import time
import Seguridad


#Clase para el inicio de sesión y registro de los médicos
class Medico():
    def __init__(self, usuario: str, contrasena: str):
        self.usuario = usuario
        self.contrasena = contrasena

    def transf_a_dic(self):
        return{
            "usuario": self.usuario,
            "contrasena": self.contrasena,
        }

def registrar_m():
    usuario = input("Introduce un nombre de usuario:")
    json = Json.Json("storage/medicos.json")
    json.load()
    if json.data == []:
        contrasena_m(usuario, json)
    else:
        for item in json.data:
            if item["usuario"]== usuario:
                print("Este usuario ya existe")
                time.sleep(1)
                return
            else:
                contrasena_m(usuario, json)
    return

def iniciar_sesion_m():
    usuario = input("Introduce tu nombre de usuario: ")
    contrasena = getpass.getpass("Introduce tu contraseña: ")
    json = Json.Json("storage/medicos.json")
    json.load()
    for item in json.data:
        if item["usuario"] == usuario and item["contrasena"] == contrasena:
            return usuario
        else:
            print("Las credenciales no son correctas")
            time.sleep(1)
            return None
    return

def comprobacion_usuario_existente():
    return

def contrasena_m(usuario, json):
    contrasena = getpass.getpass("Introduce una contraseña: ")
    if Seguridad.contrasena_robusta(contrasena):
        contrasena2 = getpass.getpass("Repite contraseña: ")
        if contrasena == contrasena2:
            crear_perfil_m(usuario, contrasena, json)
            time.sleep(1)
        else:
            print("Las contraseñas no coinciden")
            time.sleep(1)
    else:
        print("La contraseña no es segura")
        time.sleep(1)
    return

def crear_perfil_m(usuario, contrasena, json):
    data = Medico(usuario, contrasena)
    json.add_item(data.transf_a_dic())
    print("Se ha registrado exitosamente")
    return