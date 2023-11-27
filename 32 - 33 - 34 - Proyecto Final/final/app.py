#--------------------------------------------------------------------
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
#--------------------------------------------------------------------



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
            cantidad INT NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255),
            proveedor INT(4))''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
        
    #----------------------------------------------------------------
    def agregar_producto(self, codigo, descripcion, cantidad, precio, imagen, proveedor):
        # Verificamos si ya existe un producto con el mismo código
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        producto_existe = self.cursor.fetchone()
        if producto_existe:
            return False

        
        sql = "INSERT INTO productos (codigo, descripcion, cantidad, precio, imagen_url, proveedor) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (codigo, descripcion, cantidad, precio, imagen, proveedor)

        self.cursor.execute(sql, valores)        
        self.conn.commit()
        return True

    #----------------------------------------------------------------
    def consultar_producto(self, codigo):
        # Consultamos un producto a partir de su código
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        return self.cursor.fetchone()

    #----------------------------------------------------------------
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
        sql = "UPDATE productos SET descripcion = %s, cantidad = %s, precio = %s, imagen_url = %s, proveedor = %s WHERE codigo = %s"
        valores = (nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor, codigo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def listar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall()
        return productos

    #----------------------------------------------------------------
    def eliminar_producto(self, codigo):
        # Eliminamos un producto de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM productos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def mostrar_producto(self, codigo):
        # Mostramos los datos de un producto a partir de su código
        producto = self.consultar_producto(codigo)
        if producto:
            print("-" * 40)
            print(f"Código.....: {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen_url']}")
            print(f"Proveedor..: {producto['proveedor']}")
            print("-" * 40)
        else:
            print("Producto no encontrado.")


#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------
# Crear una instancia de la clase Catalogo
#catalogo = Catalogo(host='localhost', user='root', password='', database='miapp')
catalogo = Catalogo(host='localhost', user='root', password='root', database='miapp')


# catalogo.agregar_producto(1, "Televisor 25",11, 340000, "tele.jpg",1)
# catalogo.agregar_producto(2, "Notebook",11, 740000, "compu.jpg",1)
# catalogo.agregar_producto(3, "Mouse tres botones",11, 3400, "mouse.jpg",1)


# Carpeta para guardar las imagenes.
RUTA_DESTINO = './static/imagenes/'

#--------------------------------------------------------------------
@app.route("/productos", methods=["GET"])
def listar_productos():
    productos = catalogo.listar_productos()
    return jsonify(productos)


#--------------------------------------------------------------------
@app.route("/productos/<int:codigo>", methods=["GET"])
def mostrar_producto(codigo):
    producto = catalogo.consultar_producto(codigo)
    if producto:
        return jsonify(producto), 201
    else:
        return "Producto no encontrado", 404


#--------------------------------------------------------------------
@app.route("/productos", methods=["POST"])
def agregar_producto():
    #Recojo los datos del form
    codigo = request.form['codigo']
    descripcion = request.form['descripcion']
    cantidad = request.form['cantidad']
    precio = request.form['precio']
    imagen = request.files['imagen']
    proveedor = request.form['proveedor']  
    nombre_imagen=""

    # Me aseguro que el producto exista
    producto = catalogo.consultar_producto(codigo)
    if not producto: # Si no existe el producto...
        # Genero el nombre de la imagen
        nombre_imagen = secure_filename(imagen.filename)
        nombre_base, extension = os.path.splitext(nombre_imagen)
        nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
        
        if  catalogo.agregar_producto(codigo, descripcion, cantidad, precio, nombre_imagen, proveedor):
            imagen.save(os.path.join(RUTA_DESTINO, nombre_imagen))
            return jsonify({"mensaje": "Producto agregado correctamente.", "imagen": nombre_imagen}), 201
        else:
            return jsonify({"mensaje": "Error al agregar el producto."}), 500

    else:
        return jsonify({"mensaje": "Producto ya existe."}), 400
    

#--------------------------------------------------------------------
@app.route("/productos/<int:codigo>", methods=["PUT"])
def modificar_producto(codigo):
    #Recojo los datos del form
    nueva_descripcion = request.form.get("descripcion")
    nueva_cantidad = request.form.get("cantidad")
    nuevo_precio = request.form.get("precio")
    nuevo_proveedor = request.form.get("proveedor")
    imagen = request.files['imagen']

    # Procesamiento de la imagen
    nombre_imagen = secure_filename(imagen.filename)
    nombre_base, extension = os.path.splitext(nombre_imagen)
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"

    # Busco el producto guardado
    producto = producto = catalogo.consultar_producto(codigo)
    if producto: # Si existe el producto...
        imagen_vieja = producto["imagen_url"]
        # Armo la ruta a la imagen
        ruta_imagen = os.path.join(RUTA_DESTINO, imagen_vieja)

        # Y si existe la borro.
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)
    
    if catalogo.modificar_producto(codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nombre_imagen, nuevo_proveedor):
        imagen.save(os.path.join(RUTA_DESTINO, nombre_imagen))
        return jsonify({"mensaje": "Producto modificado"}), 200
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 403

#--------------------------------------------------------------------
@app.route("/productos/<int:codigo>", methods=["DELETE"])
def eliminar_producto(codigo):
    # Busco el producto guardado
    producto = catalogo.consultar_producto(codigo)
    if producto: # Si existe el producto...
        imagen_vieja = producto["imagen_url"]
        # Armo la ruta a la imagen
        ruta_imagen = os.path.join(RUTA_DESTINO, imagen_vieja)

        # Y si existe la borro.
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)

    # Luego, elimina el producto del catálogo
    if catalogo.eliminar_producto(codigo):
        return jsonify({"mensaje": "Producto eliminado"}), 200
    else:
        return jsonify({"mensaje": "Error al eliminar el producto"}), 500
    

#--------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)