import Json
import Seguridad
import Clave

#Clase para lo relacionado con los expedientes médicos
class Paciente:
    def __init__(self,
                 nombre: str,
                 apellido1: str,
                 apellido2: str,
                 edad: int,
                 sexo: str,
                 ciudad: str,
                 calle: str,
                 numero: int,
                 movil: int,
                 cuenta: str,
                 diagnostico: str):
        self.usuario = (nombre+apellido1+apellido2).lower()
        self.nombre = nombre
        self.nonce_nombre = None
        self.apellido1 = apellido1
        self.nonce_apellido1 = None
        self.apellido2 = apellido2
        self.nonce_apellido2 = None
        self.edad = edad
        self.nonce_edad = None
        self.sexo = sexo
        self.nonce_sexo = None
        self.ciudad = ciudad
        self.nonce_ciudad = None
        self.calle = calle
        self.nonce_calle = None
        self.numero = numero
        self.nonce_numero = None
        self.movil = movil
        self.nonce_movil = None
        self.cuenta = cuenta
        self.nonce_cuenta = None
        self.diagnostico = diagnostico
        self.nonce_diagnostico = None

    #Transformar los datos del paciente a diccionario para usarlo al manejar json
    def transf_a_dic(self):
        return{
            "usuario": self.usuario,
            "nombre": self.nombre,
            "nonce_nombre": self.nonce_nombre,
            "apellido1": self.apellido1,
            "nonce_apellido1": self.nonce_apellido1,
            "apellido2": self.apellido2,
            "nonce_apellido2": self.nonce_apellido2,
            "edad": self.edad,
            "nonce_edad": self.nonce_edad,
            "sexo": self.sexo,
            "nonce_sexo": self.nonce_sexo,
            "ciudad": self.ciudad,
            "nonce_ciudad": self.nonce_ciudad,
            "calle": self.calle,
            "nonce_calle": self.nonce_calle,
            "numero": self.numero,
            "nonce_numero": self.nonce_numero,
            "movil": self.movil,
            "nonce_movil": self.nonce_movil,
            "cuenta": self.cuenta,
            "nonce_cuenta": self.nonce_cuenta,
            "diagnostico": self.diagnostico,
            "nonce_diagnostico": self.nonce_diagnostico
        }

#Crear un paciente
def agregar():
    #print("Agregar paciente")
    nombre = input("Nombre del paciente: ")
    apellido1 = input("Primer apellido del paciente: ")
    apellido2 = input("Segundo apellido del paciente: ")
    edad = input("Edad del paciente: ")
    sexo = input("Sexo del paciente: ")
    ciudad = input("Ciudad donde reside el paciente: ")
    calle = input("Calle donde reside el paciente: ")
    numero = input("Número de portal del paciente: ")
    movil = input("Número de teléfono del paciente: ")
    cuenta = input("Número de cuenta bancaria del paciente: ")
    diagnostico = input("Diagnóstico del paciente: ")

    nuevo_paciente = Paciente(nombre, apellido1, apellido2, edad, sexo, ciudad,
                              calle, numero, movil, cuenta, diagnostico)
    guardar_paciente(nuevo_paciente)
    print("El paciente se ha creado correctamente\n")
    print("Presione enter para volver al menú")
    input()
    return

def cifrar_paciente(paciente):
    key = Seguridad.key_aleatoria()
    claves = Clave.Claves(paciente.usuario, key)
    claves.guardar()
    paciente.nombre, paciente.nonce_nombre = Seguridad.cifrar(paciente.nombre.encode('utf-8'), key)
    paciente.apellido1, paciente.nonce_apellido1 = Seguridad.cifrar(paciente.apellido1.encode('utf-8'), key)
    paciente.apellido2, paciente.nonce_apellido2 = Seguridad.cifrar(paciente.apellido2.encode('utf-8'), key)
    paciente.edad, paciente.nonce_edad = Seguridad.cifrar(str(paciente.edad).encode('utf-8'), key)
    paciente.sexo, paciente.nonce_sexo = Seguridad.cifrar(paciente.sexo.encode('utf-8'), key)
    paciente.ciudad, paciente.nonce_ciudad = Seguridad.cifrar(paciente.ciudad.encode('utf-8'), key)
    paciente.calle, paciente.nonce_calle = Seguridad.cifrar(paciente.calle.encode('utf-8'), key)
    paciente.numero, paciente.nonce_numero = Seguridad.cifrar(str(paciente.numero).encode('utf-8'), key)
    paciente.movil, paciente.nonce_movil = Seguridad.cifrar(str(paciente.movil).encode('utf-8'), key)
    paciente.cuenta, paciente.nonce_cuenta = Seguridad.cifrar(paciente.cuenta.encode('utf-8'), key)
    paciente.diagnostico, paciente.nonce_diagnostico = Seguridad.cifrar(paciente.diagnostico.encode('utf-8'), key)
    #print("paciente cifrado")
    #input()
    return paciente

def guardar_paciente(paciente):
    cifrar_paciente(paciente)
    json = Json.Json("storage/pacientes_expediente.json")
    data = paciente.transf_a_dic()
    json.add_item(data)
    #print("paciente guardado")
    #input()
    return

#Modificar datos de un paciente
def modificar():
    #print("Modificar paciente")
    usuario = input("Introduce el nombre de usuario que quieres modificar:")
    clave = input("Introduce el nombre de la clave del diccionario:")
    valor = input("Escribe el nuevo valor: \n")
    json = Json.Json("storage/pacientes_expediente.json")
    json.load()
    for item in json.data:
        if item["usuario"] == usuario:
            if clave in item:
                item[clave] = valor
                json.save()
                return f"Se ha modificado exitosamente."
            else:
                return f"La clave '{clave}' no existe."
    return f"No se encontró el usuario '{usuario}'."


#Buscar un paciente para obtener más información
def buscar():
    #print("Buscar paciente")
    clave = input("Introduce el nombre de la clave del diccionario:")
    valor = input("Escribe el valor: \n")
    json = Json.Json("storage/pacientes_expediente.json")
    paciente = json.find_item(valor, clave)
    print(f"Usuario: {paciente['usuario']}, \n"
          f"Nombre: {paciente['nombre']}, \n"
          f"Apellido1: {paciente['apellido1']}, \n"
          f"Apellido2: {paciente['apellido2']}, \n"
          f"Sexo: {paciente['sexo']}, \n"
          f"Edad: {paciente['edad']}, \n"
          f"Móvil: {paciente['movil']}, \n"
          f"Calle: {paciente['calle']}, \n"
          f"Numero: {paciente['numero']}, \n"
          f"Ciudad: {paciente['ciudad']}, \n"
          f"Diagnostico: {paciente['diagnostico']}, \n"
          )
    print("Pulse enter para volver al menú\n")
    input()
    return

#Mostrar lista de todos los pacientes
def mostrar():
    #print("Mostrar pacientes")
    json = Json.Json("storage/pacientes_expediente.json")
    json.load()
    if not json.data:
        print("No hay pacientes registrados.")
        return

    print("Lista de pacientes: \n")
    for i, paciente in enumerate(json.data, start=1):
        print(f"{i}. Nombre: {paciente['nombre']}, \n"
              f"   Apellido1: {paciente['apellido1']}, \n"
              f"   Apellido2: {paciente['apellido2']}, \n"
              f"   Movil: {paciente['movil']}, \n"
              )
    print("Pulse enter para volver al menú\n")
    input()
    return
