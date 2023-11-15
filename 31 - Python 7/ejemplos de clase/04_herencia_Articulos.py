#Librería: vende útiles escolares, cartulinas, y cajas de colores/pinturas
'''
class Articulo:
    def __init__(self, codigo, descripcion, precio, capacidad="", largo="", ancho="", grosor=""):
        self.codigo = codigo #Atributo común
        self.descripcion = descripcion #Atributo común
        self.precio = precio #Atributo común
        self.capacidad = capacidad #Atributo para cajas
        self.largo = largo #Atributo para cartulinas
        self.ancho = ancho #Atributo para cartulinas
        self.grosor = grosor #Atributo para cartulinas
'''
class Articulo:
    def __init__(self, codigo, descripcion, precio):
        self.codigo = codigo #Atributo común
        self.descripcion = descripcion #Atributo común
        self.precio = precio #Atributo común

    def __str__(self):
        return f'Código: {self.codigo}\nDescripción: {self.descripcion} \nPrecio: {self.precio}\n'


class Caja(Articulo):
    capacidad = "" #Atributo para cajas

    def __str__(self):
        return f'Código: {self.codigo}\nDescripción: {self.descripcion} \nPrecio: {self.precio} \nCapacidad: {self.capacidad}\n'

class Cartulina(Articulo):
    largo = "" #Atributo para cartulina
    ancho = "" #Atributo para cartulina
    grosor = "" #Atributo para cartulina

    def __str__(self):
        return f'Código: {self.codigo}\nDescripción: {self.descripcion} \nPrecio: {self.precio}\nMedidas: {self.largo}x{self.ancho} cms \nGrosor: {self.grosor} micrones\n'

#Programa principal
regla = Articulo(1234, "Regla de 20cms",50)
print(regla)

lapices = Caja(2300,"Pinturitas de colores", 575)
lapices.capacidad = "12 unidades"
print(lapices)

cartulina = Cartulina(3100,"Cartulina negra", 120)
cartulina.largo = 1
cartulina.ancho = 0.75
cartulina.grosor = 150
print(cartulina)