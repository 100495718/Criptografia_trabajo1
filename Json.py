import json
import os

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
        self.load(self.filename)
        for item in self.data:
            if value == item[key]:
                return item
        return None

    #Añadir un elemento al json
    def add_item(self, elem_to_add):
        self.load()
        self.data.append(elem_to_add)
        self.save()
