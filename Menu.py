import Pacientes

def menu():
    while True:
        print("__________CLÍNICA___________")
        print("1- Crear paciente")
        print("2- Modificar paciente")
        print("3- Mostrar todos los pacientes")
        print("4- Salir")

        opcion = input("Selecciona una opción")

        match opcion:
            case "1":
                Pacientes.agregar()
            case "2":
                Pacientes.modificar()
            case "3":
                Pacientes.mostrar()
            case "4":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida")
    return

