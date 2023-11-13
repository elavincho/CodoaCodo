class Persona: 
    variable=20

    def __init__(self, nombre):
        self.nombre=nombre

# Bloque principal
persona1=Persona("Juan") 
persona2=Persona("Ana") 
persona3=Persona("Luis") 

print(persona1.nombre) # Juan
print(persona2.nombre) # Ana
print(persona3.nombre) # Luis

print(persona1.variable) # 20
Persona.variable=5
print(persona2.variable) # 5