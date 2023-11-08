class Persona: # Creamos la clase (sustantivo 1° letra mayúscula)

    piernas = 2 # Atributo de clase

    def inicializar(self, nombre): # Método constructor
        self.nombre = nombre # Atributo de instancia

    def imprimir(self): # Método para mostrar datos
        print(f'Nombre: {self.nombre}')

# Programa principal
persona1 = Persona() # Creamos un objeto basadoe en la clase Persona
persona1.inicializar("Juan Pablo") # Llamamos al constructor con un nombre
persona1.imprimir() # Mostramos los datos

persona2 = Persona()
persona2.inicializar("Julieta")
persona2.imprimir()

print(persona1.nombre,"tiene",persona1.piernas,"piernas")
print(persona2.nombre,"tiene",persona2.piernas,"piernas")