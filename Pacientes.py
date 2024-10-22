class Paciente:
    def __init__(self, id_paciente, nombre, apellido1, apellido2, edad, sexo,
                 diagnostico, ciudad, calle, numero, cuenta ):
        self.id: id_paciente
        self.nombre: nombre
        self.apellido1: apellido1
        self.apellido2: apellido2
        self.edad: edad
        self.sexo: sexo
        self.diagnostico: diagnostico
        self.ciudad: ciudad
        self.calle: calle
        self.numero: numero
        self.cuenta: cuenta

    #Función para transformar paciente a diccionario
    def transf_a_dic(self):
        return{
            "id_paciente": self.id,
            "nombre": self.nombre,
            "apellido1": self.apellido1,
            "apellido2": self.apellido2,
            "edad": self.edad,
            "sexo": self.sexo,
            "diagnostico": self.diagnostico,
            "ciudad": self.ciudad,
            "calle": self.calle,
            "numero": self.numero,
            "cuenta": self.cuenta
        }

def agregar():
    print("Agregar paciente")
    return

def modificar():
    print("Modificar paciente")
    return

def mostrar():
    print("Mostrar pacientes")
    return