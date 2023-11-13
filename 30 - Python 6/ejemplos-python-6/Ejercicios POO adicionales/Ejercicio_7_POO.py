class Cliente:
    suspendidos=[] # Atributo de clase: Los atributos son independientes por cada objeto o instancia de la clase, es decir si definimos tres objetos de la clase Persona, todas las personas tienen un atributo nombre pero cada uno tiene un valor independiente.
                   # En algunas situaciones necesitamos almacenar datos que sean compartidos por todos los objetos de dicha clase, en esas situaciones debemos emplear variables de clase.
                   # Para definir una variable de clase lo hacemos dentro de la clase pero fuera de sus métodos:
                   # https://pythones.net/variables-de-clases/
                   
    def __init__(self,codigo,nombre):
        self.codigo=codigo #Atributo de Instancia
        self.nombre=nombre #Atributo de Instancia

    def imprimir(self):
        print(f'{self.codigo}: {self.nombre} - ', end='')
        self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("está suspendido")
        else:
            print("NO está suspendido")

    def suspender(self):
        Cliente.suspendidos.append(self.codigo)

# Bloque principal
cliente1=Cliente(1,"Juan")
cliente2=Cliente(2,"Ana")
cliente3=Cliente(3,"Diego")
cliente4=Cliente(4,"Pedro")

cliente1.suspender()
cliente4.suspender()

cliente1.imprimir()   
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

#Dos formas de mostrar la misma información
print("Suspendidos:", Cliente.suspendidos)
print("Suspendidos:")
for i in range(len(Cliente.suspendidos)):
    print(Cliente.suspendidos[i])