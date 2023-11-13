class Pelicula:

    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return f'{self.titulo} ({self.lanzamiento})'

class Catalogo:

    peliculas = []  # Esta lista contendrá objetos de la clase Pelicula

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):  # p será un objeto Pelicula
        self.peliculas.append(p)

    def mostrar(self):
        print()
        print("Catálogo de películas:")
        for p in self.peliculas:
            print(p)  # Print toma por defecto str(p)
        print()
        
#Programa principal
peli1 = Pelicula("El Padrino", 175, 1972)
print(peli1)
catalogo = Catalogo([peli1])  # Instanciamos un catálogo que contiene una pelicula
catalogo.mostrar()
catalogo.agregar(Pelicula("El Padrino: Parte 2", 202, 1974))  # Añadimos otra
catalogo.agregar(Pelicula("Titanic", 180, 1995))  # Añadimos otra

catalogo.mostrar()
# print()

