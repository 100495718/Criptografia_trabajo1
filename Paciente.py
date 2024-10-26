import getpass
import Json
import time
import Seguridad

#Clase para llevar a cabo el inicio de sesión y registro de pacientes y mantener los datos de las cuentas separados
#del expediente médico
class Paciente_usuario():
    def __init__(self, usuario: str, contrasena:str):
        self.usuario = usuario
        self.contrasena = contrasena

    def transf_a_dic(self):
        return{
            "usuario": self.usuario,
            "contrasena": self.contrasena,
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
                            data = Paciente_usuario(usuario, contrasena)
                            json_cuentas.add_item(data.transf_a_dic())
                            print("Se ha registrado exitosamente")
                            time.sleep(1)
                        else:
                            print("Las contraseñas no coinciden")
                            time.sleep(1)
                    else:
                        print("La contraseña no es segura")
                        time.sleep(1)
                else:
                    print("No se puede crear una cuenta para este usuario")
                    time.sleep(1)
        else:
            print("No se puede crear una cuenta para este usuario")
            time.sleep(1)
    else:
        for item in json_cuentas.data:
            if item["usuario"] == usuario:
                print("Ya existe una cuenta con ese usuario")
                time.sleep(1)
            else:
                if json_expedientes.data != []:
                    for item in json_expedientes.data:
                        if item["usuario"] == usuario:
                            contrasena = getpass.getpass("Introduce una contraseña: ")
                            if Seguridad.contrasena_robusta(contrasena):
                                contrasena2 = getpass.getpass("Repite contraseña: ")
                                if contrasena == contrasena2:
                                    data = Paciente_usuario(usuario, contrasena)
                                    json_cuentas.add_item(data.transf_a_dic())
                                    print("Se ha registrado exitosamente")
                                    time.sleep(1)
                                else:
                                    print("Las contraseñas no coinciden")
                                    time.sleep(1)
                            else:
                                print("La contraseña no es segura")
                                time.sleep(1)
                        else:
                            print("No se puede crear una cuenta para este usuario")
                            time.sleep(1)
                else:
                    print("No se puede crear una cuenta para este usuario")
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

def contrasena_segura_p():
    return

def comprobacion_usuario_existente():
    return

def crear_perfil_p(usuario, contrasena):
    return
