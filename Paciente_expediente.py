import Json

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
    json = Json.Json("storage/pacientes_expediente.json")
    json.add_item(data)
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
    input()
    return
