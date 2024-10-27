import re #Biblioteca para detectar expresiones regulares
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
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
    salt = os.urandom(16)
    #Configuración del algoritmo
    kdf = Scrypt(salt=salt,length=32,n=2**14,r=8,p=1)
    #Obtener hash
    hash = kdf.derive(contrasena.encode('utf-8'))
    return hash, salt

def verificar_contrasena(contrasena, hash, salt):
    # Configuración del algoritmo
    kdf = Scrypt(salt=salt,length=32,n=2**14,r=8,p=1)
    try:
        kdf.verify(contrasena.encode('utf-8'), hash)
        return True
    except Exception:
        return False

