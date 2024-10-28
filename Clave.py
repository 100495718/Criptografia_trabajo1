import Seguridad
import Json

class Claves():
    def __init__(self, usuario, key):
        self.usuario = usuario
        self.key, self.nonce = Seguridad.cifrar_clave(key)


    #Transformar los datos del paciente a diccionario
    def transf_a_dic(self):
        return{
            "usuario": self.usuario,
            "key": self.key.hex(),
            "nonce": self.nonce.hex()
        }

    #Guardar las claves en el json
    def guardar(self):
        json = Json.Json("storage/cifrado_info.json")
        json.add_item(self.transf_a_dic())
        return


