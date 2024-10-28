import json
import os

#Clase que contiene las funciones relacionadas con archivos json que  van a utilizarse en otras funciones fuera
#de esta clase
class Json():
    def __init__(self, filename):
        self.data = []
        self.filename = filename

    #Cargar archivo json
    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8", newline="") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = []
        return self.data

    #Guardar archivo json
    def save(self):
        try:
            with open(self.filename, "w", encoding="utf-8", newline="") as file:
                json.dump(self.data, file, indent=2)
        except FileNotFoundError:
            print("Error al guardar en json")

    #Buscar elemento por valor y clave en el json
    def find_item(self, value, key):
        self.load()
        for item in self.data:
            if value == item[key]:
                return item
        print("key no encontrada")
        return None

    #Añadir un elemento al json
    def add_item(self, elem_to_add):
        self.load()
        self.data.append(elem_to_add)
        self.save()

    #Borrar un elemento
    def delete_item(self, value, key):
        self.load()
        for item in self.data:
            if item[key] == value:
                self.data.remove(item)
        self.save()
