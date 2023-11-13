class Persona: 
    edad = 20

    def __init__(self, nombre):
        self.nombre=nombre

    def __str__(self):
        return f'{self.nombre} ({self.edad})'
    
# Bloque principal
persona1=Persona("Juan") 
persona2=Persona("Ana") 
persona3=Persona("Luis") 

print(persona1) # Juan (20)
print(persona2) # Ana (20)
print(persona3) # Luis (20)
print()
Persona.edad=5 #Afecta a toda la clase
print("Modificamos la variable edad (variable de CLASE) con el valor", Persona.edad)
print(persona1) # Juan (5)
print(persona2) # Ana (5)
print(persona3) # Luis (5)
print()
print("Solo modificamos la variable edad para ESTE OBJETO")
persona3.edad=25 #Afecta al objeto
print(persona3) # # Luis (25)