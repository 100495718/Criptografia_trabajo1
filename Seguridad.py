import re #Biblioteca para detectar expresiones regulares
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
#Funciones relativas a la seguridad del programa

#Algoritmo para comprobar que una contraseña es robusta
def contrasena_robusta(contrasena):
    if len(contrasena)>=8:
        if re.search(r"[a-z]", contrasena): #Detectar si tiene al menos una minúscula
            if re.search(r"[A-Z]", contrasena): #Detectar si tiene alguna mayúscula
                if re.search(r"[0-9]", contrasena): #Detectar si tiene números
                    #Detectar carácteres especiales
                    if re.search(r"[#!@$%&/()=?¿¡_.,;:{}*^<>]", contrasena):
                        return True
    return False

def derivar_contrasena(contrasena:str):
    salt = os.random(16)
    #Configuración del algoritmo PBKDF2
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=480000)
    #Obtener hash
    hash = kdf.derive(contrasena.encode('utf-8'))
    return hash, salt

def verificar_contrasena(contrasena, hash, salt):
    # Configuración del algoritmo PBKDF2
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=480000)
    try:
        kdf.verify(contrasena.encode('utf-8'), hash)
        return True
    except Exception:
        return False

