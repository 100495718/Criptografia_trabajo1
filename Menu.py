import Paciente_expediente
import Medico
import Paciente
import os
import time

#Clase para las "interfaces gráficas"
def menu():
    while True:
        borrar_pantalla()
        print("______________CLÍNICA______________")
        print("__________MENÚ PRINCIPAL___________\n")
        print("1- Iniciar sesión como médico")
        print("2- Registrarse como médico")
        print("3- Iniciar sesión como paciente")
        print("4- Registrarse como paciente")
        print("5- Salir\n")

        opcion = input("Selecciona una opción")
        print()

        match opcion:
            case "1":
                print("Inicio sesión medico")
                usuario = Medico.iniciar_sesion_m()
                if usuario != None:
                    menu_medico()
            case "2":
                print("Registro médico")
                Medico.registrar_m()
            case "3":
                print("Inicio sesión paciente")
                usuario = Paciente.iniciar_sesion_p()
                if usuario != None:
                    menu_paciente(usuario)
            case "4":
                print("Registro paciente")
                Paciente.registrar_p()
            case "5":
                print("Saliendo...")
                time.sleep(1)
                break
            case _:
                print("Opción no válida")
                time.sleep(1)

def menu_medico():
    while True:
        borrar_pantalla()
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
                Paciente_expediente.agregar()
            case "2":
                Paciente_expediente.modificar()
            case "3":
                Paciente_expediente.mostrar()
            case "4":
                Paciente_expediente.buscar()
            case "5":
                print("Volviendo al menú principal... \n")
                time.sleep(1)
                break
            case _:
                print("Opción no válida")
                time.sleep(1)

def menu_paciente(usuario):
    while True:
        borrar_pantalla()
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
                time.sleep(1)
                break
            case _:
                print("Opción no válida")
                time.sleep(1)

#Esta función sirve para despejar la pantalla en la terminal para tener una "interfaz gráfica" más limpia
#No funciona en algunas consolas de IDEs pero si en la terminal de Windows
def borrar_pantalla():
    os.system('cls')
    return