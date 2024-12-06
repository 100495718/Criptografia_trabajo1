class Firma():
    def __init__(self, usuario: str, firma):
        self.usuario = usuario
        self.firma = firma

    def transf_a_dic(self):
        return{
            "usuario": self.usuario,
            "firma": self.firma
        }