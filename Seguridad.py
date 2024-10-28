import re #Biblioteca para detectar expresiones regulares
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
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

#Algoritmos para el almacenamiento de contraseñas
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

#Algoritmos para el cifrado
def cifrar(text, key):
    nonce = os.urandom(12)
    #Configuración del algoritmo
    chacha = ChaCha20Poly1305(key)
    texto_cifrado = chacha.encrypt(nonce, text, None)
    return texto_cifrado.hex(), nonce.hex()

def cifrar_clave(clave_cifrar):
    nonce = os.urandom(12)
    with open("storage/clave.txt", "r") as File:
        clave_maestra_hex = File.read().strip()
    clave_maestra = bytes.fromhex(clave_maestra_hex)
    chacha = ChaCha20Poly1305(clave_maestra)
    cifrado = chacha.encrypt(nonce, clave_cifrar, None)
    return cifrado, nonce

def descifrar(text, key_cifrada, nonce1, nonce2):
    with open('storage/clave.txt', 'r') as File:
        clave_maestra_hex = File.read().strip()
    clave_maestra = bytes.fromhex(clave_maestra_hex)
    chacha = ChaCha20Poly1305(clave_maestra)
    clave_descifrada = chacha.decrypt(nonce2, key_cifrada, None)
    chacha = ChaCha20Poly1305(clave_descifrada)
    descifrado = chacha.decrypt(nonce1, text, None)
    return descifrado

def key_aleatoria():
    key = ChaCha20Poly1305.generate_key()
    return key