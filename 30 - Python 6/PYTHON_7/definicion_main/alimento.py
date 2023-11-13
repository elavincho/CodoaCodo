from producto import Producto

class Alimento(Producto):

    def __init__(self,referencia,nombre,descripcion,precio,productor,distribuidor):
        super().__init__(referencia, nombre, descripcion,precio)
        self.productor = productor
        self.distribuidor = distribuidor
    
    def __str__(self):
        return "Alimento: {} - {} - {} - {} - {} - {}".format(self.referencia,self.nombre,self.descripcion,self.precio,self.productor,self.distribuidor)