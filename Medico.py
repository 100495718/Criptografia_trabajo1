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
    if json.data == []: # Si no hay usuarios registrados
        contrasena = getpass.getpass("Introduce una contraseña: ")
        if Seguridad.contrasena_robusta(contrasena): #Verifico que la contraseña sea robusta
            contrasena2 = getpass.getpass("Repite contraseña: ")
            if contrasena == contrasena2:
                salt, hash = Seguridad.derivar_contrasena(contrasena) #Hash de la contraseña
                data = Medico(usuario, hash, salt) # Creo al médico con su nombre de usuario, la password hasheada y la salt utilizada para hashear dicha password
                json.add_item(data.transf_a_dic()) # Lo guardo en un JSON
                print("Se ha registrado exitosamente")
                return
            else:
                print("Las contraseñas no coinciden") # Contraseña incorrecta
                return
        else:
            print("La contraseña no es segura") # Contraseña no robusta
            return
    else:
        for item in json.data: #Si hay usuarios registrados
            if item["usuario"]== usuario:
                print("Este usuario ya existe") # Se intenta registrar un usuario ya existente
                return
            else: # Lo mismo, se establece una contraseña robusta y se crea un médico con su nickname y su password hasheada con la salt utilizada para hashear
                contrasena = getpass.getpass("Introduce una contraseña: ") # NO se muestra la contraseña por consola
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
