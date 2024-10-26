import getpass
import Json
import time

#Clase para llevar a cabo el inicio de sesión y registro de pacientes y mantener los datos de las cuentas separados
#del expediente médico
class Paciente_usuario():
    def __init__(self, usuario: str, contrasena:str):
        self.usuario = usuario
        self.contrasena = contrasena
        return

    def transf_a_dic(self):
        return{
            "usuario": self.usuario,
            "contrasena": self.contrasena,
        }

def registrar_p():
    usuario = input("Introduce un nombre de usuario:")
    json = Json.Json("storage/pacientes_expediente.json")
    json.load()
    for item in json.data:
        if item["usuario"] == usuario:
            # getpass.getpass() sirve para realizar la misma función que un input sin mostrar lo que se está escribiendo
            # No funciona en algunas consolas de IDEs pero si en la terminal de Windows
            contrasena = getpass.getpass("Introduce una contraseña: ")
            contrasena2 = getpass.getpass("Repite contraseña: ")
            if contrasena == contrasena2:
                nuevo_paciente = Paciente_usuario(usuario, contrasena)
                json2 = Json.Json("storage/pacientes.json")
                json2.load()
                json2.add_item(nuevo_paciente.transf_a_dic())
                print("Se ha creado su cuenta exitosamente")
                time.sleep(1)
            else:
                print("Las contraseñas no coinciden")
                time.sleep(1)
        else:
            print("El usuario no es correcto")
            time.sleep(1)
    return

def iniciar_sesion_p():
    usuario = input("Introduce tu nombre de usuario: ")
    contrasena = getpass.getpass("Introduce tu contraseña: ")
    json = Json.Json("storage/pacientes.json")
    json.load()
    for item in json.data:
        if item["usuario"] == usuario and item["contrasena"] == contrasena:
            return usuario
        else:
            print("Las credenciales no son correctas")
            time.sleep(1)
            return None
    return