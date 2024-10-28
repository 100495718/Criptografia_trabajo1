import Json
import Seguridad

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
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.edad = edad
        self.sexo = sexo
        self.ciudad = ciudad
        self.calle = calle
        self.numero = numero
        self.movil = movil
        self.cuenta = cuenta
        self.diagnostico = diagnostico

    #Transformar los datos del paciente a diccionario para usarlo al manejar json
    def transf_a_dic(self):
        return{
            "usuario": self.usuario,
            "nombre": self.nombre,
            "apellido1": self.apellido1,
            "apellido2": self.apellido2,
            "edad": self.edad,
            "sexo": self.sexo,
            "ciudad": self.ciudad,
            "calle": self.calle,
            "numero": self.numero,
            "movil": self.movil,
            "cuenta": self.cuenta,
            "diagnostico": self.diagnostico,
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
    data = nuevo_paciente.transf_a_dic()
    guardar_paciente(data)
    return

#Guardar datos cifrados del paciente
def guardar_paciente(data):
    datos_cifrados = {}
    claves_nonce = {}
    for item, campo in data.items():
        texto_cifrado, nonce_texto, clave_cifrada, nonce_clave = Seguridad.cifrar(str(item[campo]))
        datos_cifrados[campo] = {
            "texto_cifrado": texto_cifrado.hex(),
            "nonce_texto": nonce_texto.hex()
        }
        claves_nonce[campo] = {
            "clave_cifrada": clave_cifrada.hex(),
            "nonce_clave": nonce_clave.hex()
        }
    json_datos = Json.Json("storage/pacientes_expediente.json")
    json_datos.add_item(datos_cifrados)
    json_claves = Json.Json("storage/cifrado_info.json")
    json_claves.add_item(claves_nonce)
    return

#Cargar la información descifrada de un paciente
def cargar_paciente(paciente):
    json_expediente = Json.Json("storage/pacientes_expediente.json")
    json_expediente.load()
    json_claves = Json.Json("storage/cifrado_info.json")
    json_claves.load()
    datos_descifrados = {}
    for campo, cifrado_data in datos_cifrados.items():
        texto_cifrado = bytes.fromhex(cifrado_data["texto_cifrado"])
        nonce_texto = bytes.fromhex(cifrado_data["nonce_texto"])

        clave_cifrada = bytes.fromhex(claves_nonce[campo]["clave_cifrada"])
        nonce_clave = bytes.fromhex(claves_nonce[campo]["nonce_clave"])

        valor_descifrado = descifrar(texto_cifrado, clave_cifrada, nonce_texto, nonce_clave)
        datos_descifrados[campo] = valor_descifrado

    return datos_descifrados

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

"""
def modificar():
    usuario = input("Introduce el nombre de usuario que quieres modificar:")
    clave = input("Introduce el nombre de la clave del diccionario:")
    nuevo_valor = input("Escribe el nuevo valor: \n")

    # Cargar y descifrar los datos del paciente específico
    paciente = cargar_paciente(usuario)

    if paciente is None:
        return f"No se encontró el usuario '{usuario}'."

    # Verificar si la clave existe en el registro del paciente
    if clave in paciente:
        # Actualizar el valor en el objeto paciente y volver a cifrarlo
        paciente[clave] = nuevo_valor
        guardar_paciente(paciente)
        return f"Se ha modificado exitosamente."
    else:
        return f"La clave '{clave}' no existe."
"""

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

"""
# Función para buscar un paciente por una clave y su valor
def buscar():
    clave = input("Introduce el nombre de la clave del diccionario:")
    valor = input("Escribe el valor: \n")

    # Cargar todos los pacientes
    with open("storage/pacientes_expediente.json", "r") as file:
        pacientes_expediente = json.load(file)

    # Buscar en cada registro descifrado
    for usuario in pacientes_expediente:
        paciente = cargar_paciente(usuario)
        if paciente and paciente.get(clave) == valor:
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
                  f"Diagnostico: {paciente['diagnostico']}, \n")
            input()
            return
    print("No se encontró ningún paciente con esa información.")
    input()
"""

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

"""
# Función para mostrar todos los pacientes en la lista
def mostrar():
    with open("storage/pacientes_expediente.json", "r") as file:
        pacientes_expediente = json.load(file)

    if not pacientes_expediente:
        print("No hay pacientes registrados.")
        return

    print("Lista de pacientes: \n")
    for i, usuario in enumerate(pacientes_expediente, start=1):
        paciente = cargar_paciente(usuario)
        if paciente:
            print(f"{i}. Nombre: {paciente['nombre']}, \n"
                  f"   Apellido1: {paciente['apellido1']}, \n"
                  f"   Apellido2: {paciente['apellido2']}, \n"
                  f"   Movil: {paciente['movil']}, \n")
    input()
"""