# Instalar con pip install Flask
from flask import Flask, request, jsonify, render_template
#from flask import request

# Instalar con pip install flask-cors
from flask_cors import CORS

# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename

# No es necesario instalar, es parte del sistema standard de Python
import os
import time

# -------------------------------------------------------------------
# Definimos la clase Catalogo
# -------------------------------------------------------------------

app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas

#--------------------------------------------------------------------
class Catalogo:
    #----------------------------------------------------------------
    # Constructor de la clase
    def __init__(self, host, user, password, database):
        # Primero, establecemos una conexión sin especificar la base de datos
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()

        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

        # Una vez que la base de datos está establecida, creamos la tabla si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
            codigo INT,
            descripcion VARCHAR(255) NOT NULL,
            cantidad INT(4) NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255),
            proveedor INT(3))''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)




    # ---------------------------------------------------------------
    # Método para agregar un producto al catálogo
    # ---------------------------------------------------------------
    def agregar_producto(self, codigo, descripcion, cantidad, precio, imagen, proveedor):
        # Verificamos si el producto ya existe en el catálogo
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        producto_existe = self.cursor.fetchone()

        if producto_existe:
            return False

        
        #Sino existe, agregamos el nuevo producto a la tabla
        sql = f"INSERT INTO productos \
                (codigo, descripcion, cantidad, precio, imagen_url, proveedor) \
                VALUES \
                ({codigo}, '{descripcion}', {cantidad}, {precio}, '{imagen}', {proveedor})"
        self.cursor.execute(sql)
        self.conn.commit()
        return True



    # ---------------------------------------------------------------
    # Método para consultar un producto por código
    # ---------------------------------------------------------------   
    def consultar_producto(self, codigo):
        # Buscamos el producto en la tabla
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        return self.cursor.fetchone() #fetchone devuelve un sólo registro


    # ---------------------------------------------------------------
    # Método para modificar los detalles de un producto
    # ---------------------------------------------------------------
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
        
        sql = f"UPDATE productos SET \
                    descripcion = '{nueva_descripcion}', \
                    cantidad = {nueva_cantidad}, \
                    precio = {nuevo_precio}, \
                    imagen_url = '{nueva_imagen}', \
                    proveedor = {nuevo_proveedor} \
                WHERE codigo = {codigo}"
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.rowcount > 0 #rowCount() devuelve el número de filas afectadas por la consulta
        
        


    # ---------------------------------------------------------------
    # Método para mostrar los detalles de un producto por código
    # ---------------------------------------------------------------
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


    # ---------------------------------------------------------------
    # Método para listar todos los productos en el catálogo
    # ---------------------------------------------------------------
    def listar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall()
        return productos



    # ---------------------------------------------------------------
    # Método para eliminar un producto por código
    # ---------------------------------------------------------------
    def eliminar_producto(self, codigo):
        self.cursor.execute(f"DELETE FROM productos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0 #rowCount() devuelve el número de filas afectadas por la consulta
   


# -------------------------------------------------------------------
# Ejemplo de uso de la clase Catalogo
# -------------------------------------------------------------------
catalogo = Catalogo(host='localhost', user='root', password='root', database='miapp')


catalogo.agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500, 'teclado.jpg', 101)
catalogo.agregar_producto(2, 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', 102)
catalogo.agregar_producto(3, 'Monitor LED', 5, 25000, 'monitor.jpg', 102)



@app.route("/productos", methods=["GET"]) #GET: método para obtener respuestas a nuestras peticiones.
def listar_productos():
    productos = catalogo.listar_productos()
    return jsonify(productos)


@app.route("/productos/<int:codigo>", methods=["GET"])
def mostrar_producto(codigo):
    producto = catalogo.consultar_producto(codigo)
    if producto:
        return jsonify(producto), 201
    else:
        return "Producto no encontrado.", 404


# -------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)





# catalogo.listar_productos()
# catalogo.mostrar_producto(1)
# catalogo.eliminar_producto(2)
# catalogo.listar_productos()



#Consultamos un producto y lo mostramos
# cod_prod = int(input("Ingrese el código producto: "))
# producto = catalogo.consultar_producto(cod_prod)
# if producto:
#     print(f"Producto encontrado: {producto['codigo']} - {producto['descripcion']}")
# else:
#     print(f"Producto {cod_prod} no encontrado.")


#Modificar un producto
# catalogo.modificar_producto(1, 'Teclado Mecánico', 20, 34000, 'tecmec.jpg', 106)