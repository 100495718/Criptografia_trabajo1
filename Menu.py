import Pacientes
import os

def menu():
    #borrar_pantalla()
    while True:
        print("______________CLÍNICA______________")
        print("__________MENÚ PRINCIPAL___________\n")
        print("1- Iniciar sesión como médico")
        print("2- Registrarse como médico")
        print("3- Iniciar sesión como paciente")
        print("4- Salir\n")

        opcion = input("Selecciona una opción")
        print()

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
    #borrar_pantalla()
    while True:
        print("______________CLÍNICA______________")
        print("__________AREA DE MÉDICO___________\n")
        print("1- Crear paciente")
        print("2- Modificar datos de un paciente")
        print("3- Mostrar todos los pacientes")
        print("4- Buscar paciente")
        print("5- Salir\n")

        opcion = input("Selecciona una opción")
        print()

        match opcion:
            case "1":
                Pacientes.agregar()
            case "2":
                Pacientes.modificar()
            case "3":
                Pacientes.mostrar()
            case "4":
                Pacientes.buscar()
            case "5":
                print("Volviendo al menú principal... \n")
                break
            case _:
                print("Opción no válida")

def menu_paciente():
    #borrar_pantalla()
    while True:
        print("_______________CLÍNICA_______________")
        print("__________AREA DE PACIENTE___________\n")
        print("1- Ver mis datos")
        print("2- Modificar mis datos")
        print("3- Salir\n")

        opcion = input("Selecciona una opción")
        print()

        match opcion:
            case "1":
                print("Ver mis datos")
            case "2":
                print("Modificar mis datos")
            case "3":
                print("Volviendo al menú principal... \n")
                break
            case _:
                print("Opción no válida")

def borrar_pantalla():
    os.system('cls')
