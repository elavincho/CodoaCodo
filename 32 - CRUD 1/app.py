# -------------------------------------------------------------------
# Definimos la clase Catalogo
# -------------------------------------------------------------------

class Catalogo:
    # Lista de productos, compartida por todas las instancias de Catalogo.
    productos = []

    # ---------------------------------------------------------------
    # Método para agregar un producto al catálogo
    def agregar_producto(self, codigo, descripcion, cantidad, precio, imagen, proveedor):
        # Verificamos si el producto ya existe en el catálogo
        if self.consultar_producto(codigo):
            print("Producto existente.")
            return False

        else:
        # Creamos un nuevo producto en forma de diccionario
            nuevo_producto = {
                'codigo': codigo,
                'descripcion': descripcion,
                'cantidad': cantidad,
                'precio': precio,
                'imagen': imagen,
                'proveedor': proveedor
            }
        
        # Agregamos el nuevo producto a la lista de productos en el catálogo
            self.productos.append(nuevo_producto)
            return True
    
    # ---------------------------------------------------------------
    # Método para consultar un producto por código
    def consultar_producto(self, codigo):
        # Buscamos el producto en la lista de productos
        for producto in self.productos:
            if producto['codigo'] == codigo:
                return producto
        return False
    
    # ---------------------------------------------------------------
    # Método para modificar los detalles de un producto
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                # Actualizamos los detalles del producto con los nuevos valores
                producto['descripcion'] = nueva_descripcion
                producto['cantidad'] = nueva_cantidad
                producto['precio'] = nuevo_precio
                producto['imagen'] = nueva_imagen
                producto['proveedor'] = nuevo_proveedor
                return True
        return False
    
    # ---------------------------------------------------------------
    # Método para listar todos los productos en el catálogo
    def listar_productos(self):
        # Imprimimos un encabezado
        print("-" * 50)
        # Recorremos la lista de productos e imprimimos sus detalles
        for producto in self.productos:
            print(f"Código.....: {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen']}")
            print(f"Proveedor..: {producto['proveedor']}")
            print("-" * 50)

    # ---------------------------------------------------------------
    # Método para eliminar un producto por código
    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                # Eliminamos el producto de la lista de productos
                self.productos.remove(producto)
                print("Producto eliminado correctamente!")
                return True
        return False
    
    # ---------------------------------------------------------------
    # Método para mostrar los detalles de un producto por código
    def mostrar_producto(self, codigo):
        # Consultamos el producto por su código
        producto = self.consultar_producto(codigo)
        if producto:
            # Imprimimos los detalles del producto
            print("-" * 50)
            print(f"Código.....: {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen']}")
            print(f"Proveedor..: {producto['proveedor']}")
            print("-" * 50)
        else:
            print("Producto no encontrado.")

# -------------------------------------------------------------------
# Ejemplo de uso de la clase Catalogo
# -------------------------------------------------------------------
catalogo = Catalogo()
catalogo.agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500, 'teclado.jpg', 101)
catalogo.agregar_producto(2, 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', 102)
catalogo.agregar_producto(3, 'Monitor 19 Pulgadas', 6, 12000, 'monitor.jpg', 105)
catalogo.agregar_producto(4, 'Gabinete Gamer', 12, 8500, 'gabinete.jpg', 102)
catalogo.agregar_producto(5, 'Parlantes USB 32 Wats', 9, 900, 'parlantes.jpg', 101)
catalogo.agregar_producto(6, 'MicroProcesador AMD 9500 G', 10, 105000, 'procesador.jpg', 108)
print("")
catalogo.listar_productos()
print("")
catalogo.mostrar_producto(3)
print("")
catalogo.mostrar_producto(9)
print("")
catalogo.eliminar_producto(4)
print("")
catalogo.listar_productos()