import Json
import Seguridad
import Clave

#Clase para lo relacionado con los expedientes médicos
class Paciente:
    def __init__(self,
                 usuario: str,
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

    #Transformar los datos del paciente a diccionario
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

#Función para transformar un diccionario con datos de un paciente en un objeto Paciente
def trans_a_obj(dic):
    return Paciente(dic["nombre"], dic["apellido1"], dic["apellido2"],dic["edad"], dic["sexo"],
                    dic["ciudad"], dic["calle"], dic["numero"], dic["movil"], dic["cuenta"], dic["diagnostico"])

#Crear un paciente
def agregar():
    #print("Agregar paciente")
    usuario = input("Nombre de usuario para el paciente: ")
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

    nuevo_paciente = Paciente(usuario, nombre, apellido1, apellido2, edad, sexo, ciudad,
                              calle, numero, movil, cuenta, diagnostico)
    guardar_paciente(nuevo_paciente)
    print("\nEl paciente se ha creado correctamente\n")
    return

#Algoritmo para cifrar datos de un paciente
def cifrar_paciente(paciente):
    #Carga del json donde se guardarán las claves del cifrado
    json = Json.Json("storage/cifrado_info.json")

    #Si ya tenia claves las elimino, esto se usará en futuras funciones
    if json.find_item(paciente.usuario, "usuario") != None:
        json.delete_item(paciente.usuario, "usuario")

    #Genero la clave simétrica
    key = Seguridad.key_aleatoria()

    #Guardo la key cifrada con la clave maestra y el nonce
    claves = Clave.Claves(paciente.usuario, key)
    claves.guardar()

    #Cifro los datos
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
    return paciente

#Función para descifrar datos de un paciente
def descifrar_paciente(paciente):
    #Carga del json donde están las claves del cifrado
    json_claves = Json.Json("storage/cifrado_info.json")
    json_claves.load()

    #Localizar las claves del paciente
    claves = json_claves.find_item(paciente.usuario, "usuario")
    key = bytes.fromhex(claves["key"])
    nonce = bytes.fromhex(claves["nonce"])

    #Descifrar datos
    paciente.nombre = Seguridad.descifrar(bytes.fromhex(paciente.nombre), key, bytes.fromhex(paciente.nonce_nombre), nonce).decode('utf-8')
    paciente.apellido1 = Seguridad.descifrar(bytes.fromhex(paciente.apellido1), key, bytes.fromhex(paciente.nonce_apellido1), nonce).decode('utf-8')
    paciente.apellido2 = Seguridad.descifrar(bytes.fromhex(paciente.apellido2), key, bytes.fromhex(paciente.nonce_apellido2), nonce).decode('utf-8')
    paciente.edad = Seguridad.descifrar(bytes.fromhex(paciente.edad), key, bytes.fromhex(paciente.nonce_edad), nonce).decode('utf-8')
    paciente.sexo = Seguridad.descifrar(bytes.fromhex(paciente.sexo), key, bytes.fromhex(paciente.nonce_sexo), nonce).decode('utf-8')
    paciente.ciudad = Seguridad.descifrar(bytes.fromhex(paciente.ciudad), key, bytes.fromhex(paciente.nonce_ciudad), nonce).decode('utf-8')
    paciente.calle = Seguridad.descifrar(bytes.fromhex(paciente.calle), key, bytes.fromhex(paciente.nonce_calle), nonce).decode('utf-8')
    paciente.numero = Seguridad.descifrar(bytes.fromhex(paciente.numero), key, bytes.fromhex(paciente.nonce_numero), nonce).decode('utf-8')
    paciente.movil = Seguridad.descifrar(bytes.fromhex(paciente.movil), key, bytes.fromhex(paciente.nonce_movil), nonce).decode('utf-8')
    paciente.cuenta = Seguridad.descifrar(bytes.fromhex(paciente.cuenta), key, bytes.fromhex(paciente.nonce_cuenta), nonce).decode('utf-8')
    return paciente

#Función para guardar un expediente en el json
def guardar_paciente(paciente):
    cifrar_paciente(paciente)
    json = Json.Json("storage/pacientes_expediente.json")
    data = paciente.transf_a_dic()
    json.add_item(data)
    return

#Mostrar lista de todos los pacientes
def mostrar():
    #Carga del .json donde están los expedientes
    json_expedientes = Json.Json("storage/pacientes_expediente.json")
    json_expedientes.load()

    #Carga del .json donde están las claves del cifrado
    json_claves = Json.Json("storage/cifrado_info.json")
    json_claves.load()
    #Detectar si hay expedientes antes de hacer el bucle
    if not json_expedientes.data:
        print("No hay pacientes registrados.")
        return
    for item in json_expedientes.data:
        usuario = item["usuario"]

        #Localizar las claves para cada usuario
        claves = json_claves.find_item(usuario, "usuario")
        key = bytes.fromhex(claves["key"])
        nonce = bytes.fromhex(claves["nonce"])

        #Descifrar los datos
        nombre = Seguridad.descifrar(bytes.fromhex(item["nombre"]), key, bytes.fromhex(item["nonce_nombre"]), nonce)
        apellido1 = Seguridad.descifrar(bytes.fromhex(item["apellido1"]), key, bytes.fromhex(item["nonce_apellido1"]), nonce)
        apellido2 = Seguridad.descifrar(bytes.fromhex(item["apellido2"]), key, bytes.fromhex(item["nonce_apellido2"]), nonce)

        #Transformar la información descifrada a texto normal
        nombre_descifrado = nombre.decode('utf-8')
        apellido1_descifrado = apellido1.decode('utf-8')
        apellido2_descifrado = apellido2.decode('utf-8')

        #Imprimir los datos por pantalla
        print(f"Usuario: {usuario}\nNombre completo: {nombre_descifrado} {apellido1_descifrado} {apellido2_descifrado}\n")
    return

#Función para mostrar algunos datos de un único paciente
def mostrar_datos_paciente(usuario):
    #Carga del json donde están los datos
    json_expedientes = Json.Json("storage/pacientes_expediente.json")
    json_expedientes.load()

    #Carga del json donde está la clave del cifrado
    json_claves = Json.Json("storage/cifrado_info.json")
    json_claves.load()

    #Localizar expediente
    paciente = json_expedientes.find_item(usuario, "usuario")

    #Localizar claves necesarias para descifrar
    claves = json_claves.find_item(usuario, "usuario")
    key = bytes.fromhex(claves["key"])
    nonce = bytes.fromhex(claves["nonce"])

    #Descifrar los datos almacenados en hexadecimal en archivos .json
    nombre = Seguridad.descifrar(bytes.fromhex(paciente["nombre"]), key, bytes.fromhex(paciente["nonce_nombre"]), nonce)
    apellido1 = Seguridad.descifrar(bytes.fromhex(paciente["apellido1"]), key, bytes.fromhex(paciente["nonce_apellido1"]),nonce)
    apellido2 = Seguridad.descifrar(bytes.fromhex(paciente["apellido2"]), key, bytes.fromhex(paciente["nonce_apellido2"]),nonce)
    edad = Seguridad.descifrar(bytes.fromhex(paciente["edad"]), key, bytes.fromhex(paciente["nonce_edad"]), nonce)
    sexo = Seguridad.descifrar(bytes.fromhex(paciente["sexo"]), key, bytes.fromhex(paciente["nonce_sexo"]), nonce)
    movil = Seguridad.descifrar(bytes.fromhex(paciente["movil"]), key, bytes.fromhex(paciente["nonce_movil"]), nonce)
    diagnostico = Seguridad.descifrar(bytes.fromhex(paciente["diagnostico"]), key, bytes.fromhex(paciente["nonce_diagnostico"]),nonce)

    #Transformar los datos descifrados a texto normal
    nombre_descifrado = nombre.decode('utf-8')
    apellido1_descifrado = apellido1.decode('utf-8')
    apellido2_descifrado = apellido2.decode('utf-8')
    edad_descifrado = edad.decode('utf-8')
    sexo_descifrado = sexo.decode('utf-8')
    movil_descifrado = movil.decode('utf-8')
    diagnostico_descifrado = diagnostico.decode('utf-8')

    #Imprimir por pantalla los datos
    print(f"Nombre: {nombre_descifrado}")
    print(f"Primer apellido: {apellido1_descifrado}")
    print(f"Segundo apellido: {apellido2_descifrado}")
    print(f"Edad: {edad_descifrado}")
    print(f"Sexo: {sexo_descifrado}")
    print(f"Movil: {movil_descifrado}")
    print(f"Diagnostico: {diagnostico_descifrado}")
    return

#Función para que los médicos obtengan más información de un paciente
def buscar():
    usuario = input("Introduce el nombre de usuario del paciente: ")
    mostrar_datos_paciente(usuario)
    return

#______________________________________FUNCIONES EN DESARROLLO_________________________________________

"""
#Buscar un paciente para obtener más información
def buscar():
    #print("Buscar paciente")
    usuario = input("Introduce el nombre de usuario del paciente: ")
    json = Json.Json("storage/pacientes_expediente.json")
    paciente = json.find_item(usuario, "usuario")
    if paciente == None:
        print("Ese usuario no existe")
        input()
        return
    else:
        json_claves = Json.Json("storage/claves_expediente.json")
        json_claves.load()
        claves = json_claves.find_item(usuario, "usuario")
        if claves == None:
            print("Clave para descifrar no encontrada")
            input()
            return
        key = bytes.fromhex(claves["key"])
        nonce = bytes.fromhex(claves["nonce"])

        nombre = Seguridad.descifrar(bytes.fromhex(item["nombre"]), key, bytes.fromhex(item["nonce_nombre"]), nonce)
        apellido1 = Seguridad.descifrar(bytes.fromhex(item["apellido1"]), key, bytes.fromhex(item["nonce_apellido1"]),nonce)
        apellido2 = Seguridad.descifrar(bytes.fromhex(item["apellido2"]), key, bytes.fromhex(item["nonce_apellido2"]),nonce)
        edad = Seguridad.descifrar(bytes.fromhex(item["edad"]), key, bytes.fromhex(item["nonce_edad"]), nonce)
        sexo = Seguridad.descifrar(bytes.fromhex(item["sexo"]), key, bytes.fromhex(item["nonce_sexo"]),nonce)
        movil = Seguridad.descifrar(bytes.fromhex(item["movil"]), key, bytes.fromhex(item["nonce_movil"]),nonce)
        diagnostico = Seguridad.descifrar(bytes.fromhex(item["diagnostico"]), key, bytes.fromhex(item["nonce_diagnostico"]), nonce)

        nombre_descifrado = nombre.decode('utf-8')
        apellido1_descifrado = apellido1.decode('utf-8')
        apellido2_descifrado = apellido2.decode('utf-8')
        edad_descifrado = edad.decode('utf-8')
        sexo_descifrado = sexo.decode('utf-8')
        movil_descifrado = movil.decode('utf-8')
        diagnostico_descifrado = diagnostico.decode('utf-8')

        print(f"Nombre: {nombre_descifrado}")
        print(f"Apellido1: {apellido1_descifrado}")
        print(f"Apellido2: {apellido2_descifrado}")
        print(f"Edad: {edad_descifrado}")
        print(f"Sexo: {sexo_descifrado}")
        print(f"Movil: {movil_descifrado}")
        print(f"Diagnostico: {diagnostico_descifrado}")
        print("\nPulse enter para volver al menú")
    return"""

"""
#Modificar datos de un paciente
def modificar():
    #print("Modificar paciente")
    json = Json.Json("storage/pacientes_expediente.json")
    json.load()
    json_claves = Json.Json("storage/cifrado_info.json")
    json_claves.load()
    usuario = input("Introduce el nombre de usuario que quieres modificar:")
    paciente_dic = json.find_item(usuario, "usuario")
    if paciente_dic == None:
        print("Este paciente no existe")
        input()
        return
    clave = input("Introduce el nombre de la clave del diccionario:")
    if clave not in ["diagnostico", "nombre", "apellido1", "apellido2", "edad", "sexo"]:
        print("Ese dato no se puede modificar o no existe")
        input()
        return
    valor = input("Escribe el nuevo valor: \n")
    paciente = trans_a_obj(paciente_dic)
    paciente_cifrado = cifrar_paciente(paciente)
    paciente_descifrado = descifrar_paciente(paciente_cifrado)
    paciente_descifrado.transf_a_dic()[clave] = valor
    json.delete_item(usuario, "usuario")
    json_claves.delete_item(usuario, "usuario")
    guardar_paciente(paciente_descifrado)
    print("Pulse enter para volver al menú")
    input()
    return"""