import Json

class Paciente:
    def __init__(self,
                 #id_paciente: str,
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
        #self.id: id_paciente
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

    def transf_a_dic(self):
        return{
            #"id_paciente": self.id,
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
    json = Json.Json("Pacientes.json")
    json.add_item(data)
    return

def modificar():
    print("Modificar paciente")
    return

#Mostrar lista de todos los pacientes, (los espacios y los saltos de linea del print son estéticos)
def mostrar():
    #print("Mostrar pacientes")
    json = Json.Json("Pacientes.json")
    json.load()
    if not json.data:
        print("No hay pacientes registrados.")
        return

    print("Lista de pacientes: \n")
    for i, paciente in enumerate(json.data, start=1):
        print(f"{i}. Nombre: {paciente['nombre']}, \n"
              f"   Apellido1: {paciente['apellido1']}, \n"
              f"   Apellido2: {paciente['apellido2']}, \n"
              f"   Edad: {paciente['edad']}, \n"
              f"   Sexo: {paciente['sexo']}, \n"
              f"   Ciudad: {paciente['ciudad']}, \n"
              f"   Calle: {paciente['calle']}, \n"
              f"   Número: {paciente['numero']}, \n"
              f"   Movil: {paciente['movil']}, \n"
              f"   Cuenta: {paciente['cuenta']}, \n"
              f"   Diagnóstico: {paciente['diagnostico']}"
              )
    return