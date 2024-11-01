import Json
import getpass
import time
import Seguridad

#Clase para el inicio de sesión y registro de los médicos
class Medico():
    def __init__(self, usuario: str, hash, salt):
        self.usuario = usuario
        self.hash = hash.hex()
        self.salt = salt.hex()

    def transf_a_dic(self):
        return{
            "usuario": self.usuario,
            "hash": self.hash,
            "salt": self.salt
        }

def registrar_m():
    usuario = input("Introduce un nombre de usuario:")
    json = Json.Json("storage/medicos.json")
    json.load()
    if json.data == []:
        contrasena = getpass.getpass("Introduce una contraseña: ")
        if Seguridad.contrasena_robusta(contrasena):
            contrasena2 = getpass.getpass("Repite contraseña: ")
            if contrasena == contrasena2:
                salt, hash = Seguridad.derivar_contrasena(contrasena)
                data = Medico(usuario, hash, salt)
                json.add_item(data.transf_a_dic())
                print("Se ha registrado exitosamente")
                return
            else:
                print("Las contraseñas no coinciden")
                return
        else:
            print("La contraseña no es segura")
            return
    else:
        for item in json.data:
            if item["usuario"]== usuario:
                print("Este usuario ya existe")
                return
            else:
                contrasena = getpass.getpass("Introduce una contraseña: ")
                if Seguridad.contrasena_robusta(contrasena):
                    contrasena2 = getpass.getpass("Repite contraseña: ")
                    if contrasena == contrasena2:
                        salt, hash = Seguridad.derivar_contrasena(contrasena)
                        data = Medico(usuario, hash, salt)
                        json.add_item(data.transf_a_dic())
                        print("Se ha registrado exitosamente")
                        return
                    else:
                        print("Las contraseñas no coinciden")
                        return
                else:
                    print("La contraseña no es segura")
                    return
    return

def iniciar_sesion_m():
    usuario = input("Introduce tu nombre de usuario: ")
    contrasena = getpass.getpass("Introduce tu contraseña: ")
    json = Json.Json("storage/medicos.json")
    json.load()
    item = json.find_item(usuario, "usuario")
    if item == None:
        print("No encontrado")
        return
    salt = bytes.fromhex(item["salt"])
    hash = bytes.fromhex(item["hash"])
    if Seguridad.verificar_contrasena(contrasena, salt, hash):
        return usuario
    else:
        print("Las credenciales no son correctas")
        return None
    return
