import re #Biblioteca para detectar expresiones regulares
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
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
#Algoritmo Scrypt
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

#Algoritmos para el cifrado, cifrado híbrido
#Generar clave pública y privada
def generate_rsa_keys():
    clave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    clave_publica = clave_privada.public_key()
    return clave_privada, clave_publica


#Cifrado
def cifrar(clave_publica, datos_a_cifrar):
    # Generar clave simétrica
    clave_simetrica = AESGCM.generate_key(bit_length=128)
    aesgcm = AESGCM(clave_simetrica)

    # Generar un nonce para AES-GCM
    nonce = os.urandom(12)

    # Cifrar con AES-GCM
    datos_cifrados = aesgcm.encrypt(nonce, datos_a_cifrar, None)

    # Cifrar la clave simétrica con RSA
    clave_simetrica_cifrada = clave_publica.encrypt(
        clave_simetrica,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return nonce, datos_cifrados, clave_simetrica_cifrada


#Descifrado
def descifrar(clave_privada, nonce, dato_cifrado, clave_simetrica_cifrada):
    # Descifrar clave simétrica con RSA
    clave_simetrica = clave_privada.decrypt(
        clave_simetrica_cifrada,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Descifrar datos cifrados con AES-GCM
    aesgcm = AESGCM(clave_simetrica)
    datos_descifrados = aesgcm.decrypt(nonce, dato_cifrado, None)

    return datos_descifrados