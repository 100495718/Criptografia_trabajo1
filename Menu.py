import Pacientes

def menu():
    while True:
        print("__________CLÍNICA___________")
        print("1- Iniciar sesión como médico")
        print("2- Registrarse como médico")
        print("3- Iniciar sesión como paciente")
        print("4- Registrarse como paciente")
        print("5- Salir")

        opcion = input("Selecciona una opción")

        match opcion:
            case "1":
                print("Inicio sesión medico")
                menu_medico()
            case "2":
                print("Registro médico")
            case "3":
                print("Inicio sesión paciente")
                menu_paciente()
            case "4":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida")

def menu_medico():
    while True:
        print("__________AREA DE MÉDICO___________")
        print("1- Crear paciente")
        print("2- Modificar datos de un paciente")
        print("3- Mostrar todos los pacientes")
        print("4- Buscar paciente")
        print("5- Salir")

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

def menu_paciente():
    while True:
        print("__________AREA DE PACIENTE___________")
        print("1- Ver mis datos")
        print("2- Modificar mis datos")
        print("3- Salir")

        opcion = input("Selecciona una opción")
        match opcion:
            case "1":
                print("Ver mis datos")
            case "2":
                print("Modificar mis datos")
            case "3":
                print("Saliendo...")
            case _:
                print("Opción no válida")