import Json
import Seguridad
import Firma
from cryptography.hazmat.primitives import serialization

#Clase para lo relacionado con los expedientes médicos
class Paciente:
    def __init__(self,
                 usuario:str,
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
        self.usuario = usuario
        self.clave_sesion = None
        self.clave_publica = None
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
            "clave_sesion": self.clave_sesion,
            "clave_publica": self.clave_publica,
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
    return Paciente(dic["usuario"], dic["nombre"], dic["apellido1"], dic["apellido2"],dic["edad"], dic["sexo"],
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
    #Genero claves para el cifrado
    clave_privada, clave_publica = Seguridad.generate_claves_rsa()

    #Cifro los datos
    atributos = ["nombre", "apellido1", "apellido2", "edad", "sexo", "ciudad", "calle",
                 "numero", "movil", "cuenta", "diagnostico"]

    paciente_cifrado = {"usuario": paciente.usuario}
    info_cifrado = {"usuario": paciente.usuario,
    "clave_privada": clave_privada.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ).hex()}

    json_cifrado = Json.Json("storage/claves_priv_pacientes.json")
    json_cifrado.load()
    json_cifrado.add_item(info_cifrado)

    aesgcm, clave_sesion_cifrada, clave_sesion = Seguridad.generate_clave_sesion(clave_publica)

    for item in atributos:
        dato = str(getattr(paciente, item)).encode("utf-8")
        nonce, dato_cifrado = Seguridad.cifrar(aesgcm, dato)

        paciente_cifrado[item] = dato_cifrado.hex()
        paciente_cifrado[f"nonce_{item}"] = nonce.hex()

    paciente_cifrado["clave_sesion"] = clave_sesion_cifrada.hex()
    paciente_cifrado["clave_publica"] = clave_publica.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).hex()

    return paciente_cifrado, clave_privada

#Función para descifrar datos de un paciente
def descifrar_paciente(paciente):
    # Carga del json donde están las claves del cifrado
    json_claves = Json.Json("storage/claves_priv_pacientes.json")
    json_claves.load()
    json_paciente = Json.Json("storage/pacientes_expediente.json")
    json_paciente.load()

    paciente_dic = paciente.transf_a_dic()
    usuario = paciente_dic["usuario"]
    claves = json_claves.find_item(usuario, "usuario")
    paciente_cifrado = json_paciente.find_item(usuario, "usuario")

    if claves is None:
        print(f"Error: No se encontraron claves para el paciente con usuario {usuario}")
        return None

    clave_privada = serialization.load_pem_private_key(
        bytes.fromhex(claves["clave_privada"]),
        password=None
    )
    atributos = ["nombre", "apellido1", "apellido2", "edad", "sexo", "ciudad", "calle",
                 "numero", "movil", "cuenta", "diagnostico"]

    # Descifrar la clave de sesión con la clave privada RSA
    clave_sesion_cifrada = bytes.fromhex(paciente_cifrado["clave_sesion"])
    aesgcm = Seguridad.descifrar_clave_sesion(clave_sesion_cifrada, clave_privada)

    for item in atributos:
        # Recuperar los datos cifrados y el nonce
        dato_cifrado = bytes.fromhex(paciente_cifrado[item])
        nonce = bytes.fromhex(paciente_cifrado[f"nonce_{item}"])

        # Descifrar el atributo utilizando la clave de sesión
        dato_descifrado = Seguridad.descifrar(aesgcm, nonce, dato_cifrado)

        # Actualizar el atributo del paciente con el dato descifrado
        setattr(paciente, item, dato_descifrado.decode("utf-8"))
    return paciente

#Función para guardar un expediente en el json
def guardar_paciente(paciente):
    #Cifrar paciente
    paciente_cifrado, clave_privada = cifrar_paciente(paciente)

    #Cargar json para almacenar datos de paciente y para almacenar firma
    json_expediente= Json.Json("storage/pacientes_expediente.json")
    json_firma = Json.Json("storage/pacientes_firma.json")

    #Firmar datos del paciente
    firma, paciente_hasehado = firmar_datos(paciente_cifrado, clave_privada)
    print("datos firmados")
    print(paciente_hasehado)
    firma_data = Firma.Firma(paciente.usuario, firma)

    #Verificar firma
    verificar_firma(clave_privada, bytes.fromhex(firma_data.firma.hex()), paciente_hasehado)
    print("Firma verificada")
    #Guardar firma y paciente
    json_expediente.add_item(paciente_cifrado)
    json_firma.add_item(firma_data.transf_a_dic())
    return

#Mostrar lista de todos los pacientes con nombre y apellidos
def mostrar():
    json_expedientes = Json.Json("storage/pacientes_expediente.json")
    json_expedientes.load()

    if not json_expedientes.data:
        print("No hay pacientes registrados.")
        return

    indice = 1
    for item in json_expedientes.data:
        paciente = trans_a_obj(item)
        paciente = descifrar_paciente(paciente)
        print(f"{indice}-Nombre completo: {paciente.nombre} {paciente.apellido1} {paciente.apellido2}")
        indice += 1
    return

#Función para mostrar algunos datos de un único paciente (nombre, apellidos, edad, sexo, movil y diagnostico)
def mostrar_datos_paciente(usuario):
    # Carga del json donde están los datos cifrados del paciente
    json_expedientes = Json.Json("storage/pacientes_expediente.json")
    json_expedientes.load()

    # Localizar expediente del paciente por su usuario
    paciente_cifrado = json_expedientes.find_item(usuario, "usuario")

    if not paciente_cifrado:
        print(f"No se encontró un paciente con el usuario {usuario}")
        return

    # Descifrar los datos del paciente
    paciente = trans_a_obj(paciente_cifrado)
    paciente = descifrar_paciente(paciente)

    # Mostrar los datos descifrados
    print(f"Nombre completo: {paciente.nombre} {paciente.apellido1} {paciente.apellido2}")
    print(f"Edad: {paciente.edad}")
    print(f"Sexo: {paciente.sexo}")
    print(f"Diagnóstico: {paciente.diagnostico}")
    return

#Función para que los médicos obtengan más información de un paciente
def buscar():
    usuario = input("Introduce el nombre de usuario del paciente: ")
    mostrar_datos_paciente(usuario)
    return

#Función para firmar los datos de un paciente
def firmar_datos(paciente, clave_privada):
    paciente_hasheado = Seguridad.hashear_paciente(paciente)
    firma = Seguridad.generar_firma(paciente_hasheado, clave_privada)
    return firma, paciente_hasheado

#Función para comprobar la firma de los datos de un paciente
def verificar_firma(clave_privada, firma, paciente_hasheado):
    Seguridad.verificacion_firma(clave_privada, firma, paciente_hasheado)
    return