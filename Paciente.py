import getpass
import Json
import Seguridad

#Clase para llevar a cabo el inicio de sesión y registro de pacientes y mantener los datos de las cuentas separados
#del expediente médico
class Paciente_usuario():
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

def registrar_p():
    usuario = input("Introduce un nombre de usuario:")
    json_cuentas = Json.Json("storage/pacientes.json")
    json_cuentas.load()
    json_expedientes = Json.Json("storage/pacientes_expediente.json")
    json_expedientes.load()
    if json_cuentas.data == []:
        if json_expedientes.data != []:
            for item in json_expedientes.data:
                if item["usuario"] == usuario:
                    contrasena = getpass.getpass("Introduce una contraseña: ")
                    if Seguridad.contrasena_robusta(contrasena):
                        contrasena2 = getpass.getpass("Repite contraseña: ")
                        if contrasena == contrasena2:
                            salt, hash = Seguridad.derivar_contrasena(contrasena)
                            data = Paciente_usuario(usuario, hash, salt)
                            json_cuentas.add_item(data.transf_a_dic())
                            print("Se ha registrado exitosamente")
                            input()
                            return
                        else:
                            print("Las contraseñas no coinciden")
                            input()
                            return
                    else:
                        print("La contraseña no es segura")
                        input()
                        return
            else:
                print("No se puede crear una cuenta para este usuario")
                input()
                return
    else:
        for item in json_cuentas.data:
            if item["usuario"] == usuario:
                print("Ya existe una cuenta con ese usuario")
                input()
                return
            else:
                if json_expedientes.data != []:
                    for item in json_expedientes.data:
                        if item["usuario"] == usuario:
                            contrasena = getpass.getpass("Introduce una contraseña: ")
                            if Seguridad.contrasena_robusta(contrasena):
                                contrasena2 = getpass.getpass("Repite contraseña: ")
                                if contrasena == contrasena2:
                                    salt, hash = Seguridad.derivar_contrasena(contrasena)
                                    data = Paciente_usuario(usuario, hash, salt)
                                    json_cuentas.add_item(data.transf_a_dic())
                                    print("Se ha registrado exitosamente")
                                    input()
                                    return
                                else:
                                    print("Las contraseñas no coinciden")
                                    input()
                                    return
                            else:
                                print("La contraseña no es segura")
                                input()
                                return
                    else:
                        print("No se puede crear una cuenta para este usuario")
                        input()
                        return
    return

def iniciar_sesion_p():
    usuario = input("Introduce tu nombre de usuario: ")
    contrasena = getpass.getpass("Introduce tu contraseña: ")
    json = Json.Json("storage/pacientes.json")
    json.load()
    for item in json.data:
        if item["usuario"] == usuario:
            salt = bytes.fromhex(item["salt"])
            hash = bytes.fromhex(item["hash"])
            if Seguridad.verificar_contrasena(contrasena, salt, hash):
                return usuario
            else:
                print("Las credenciales no son correctas")
                time.sleep(1)
                return None
    return

