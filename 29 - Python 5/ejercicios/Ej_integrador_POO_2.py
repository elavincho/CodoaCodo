class Producto:  # Creamos la clase
    nro_productos = 0  # Cantidad de productos
    categoria = ""

    # Constructor
    def __init__(self, descripcion, precio):
        self.descripcion = descripcion
        self.precio = precio
        Producto.nro_productos += 1  # Agregamos un producto

    # Mostrar datos del objeto
    def __str__(self):
        return f'Descripción: {self.descripcion} - Precio $ {self.precio}'

    # Damos de baja al producto
    def __del__(self):
        Producto.nro_productos -= 1  # Restamos un producto
        print(f'Producto {self.descripcion} dado de baja - Restan: {Producto.nro_productos}')
    
    def mostrar_categoria(self):  # Categoría del producto según precio
        print(f'La categoría del producto {self.descripcion} es:', end=' ')
        if self.precio >= 100:
            print("A")
        elif self.precio >= 50:
            print("B")
        else:
            print("C")

# Programa principal
producto1 = Producto("Azúcar", 120)
producto2 = Producto("Mayonesa", 80)
producto3 = Producto("Caramelos", 30)

print(producto1)
print(producto2)
print(producto3)

producto1.mostrar_categoria()
producto2.mostrar_categoria()
producto3.mostrar_categoria()

input("Pulse enter para salir")

print(producto1)
print(producto2)
print(producto3)