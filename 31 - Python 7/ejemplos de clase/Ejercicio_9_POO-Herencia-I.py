class Padre(): #Superclase
    def __init__(self):
        self.apellido = "Argento"
    
    def llevar(self):
        print(f'Papá me lleva al colegio')
    
class Hijo(Padre): #Subclase
    nombre = ""

    def estudiar(self):
        print(f'Soy {self.nombre} y estoy en el estudiando en el colegio')

hijo1 = Hijo() # Instancia de Hijo
hijo1.nombre = "Luis"
hijo1.llevar() # Método del lpadre
hijo1.estudiar() # Método propio
print(f'{hijo1.nombre} {hijo1.apellido}') # Imprimimos atributos