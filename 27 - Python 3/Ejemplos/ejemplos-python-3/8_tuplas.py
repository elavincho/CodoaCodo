print("****** TUPLAS ******")

#Creación de tuplas
vacia = () # tupla vacía
tupla_uno = 'Juan Pablo', # tupla con un valor
tupla_dos = ('Juan', 37, False) # mixtas
tupla_tres = 'Luciana', 56, (1998,5,26) # Tupla anidada
tupla_cuatro = ('Rivadavia', 3567, ['Calle 1', 'Calle2']) # Tupla con lista

print(vacia)
print(tupla_uno)
print(tupla_dos)
print(tupla_tres)
print(tupla_cuatro)
print()

#Acceso a elementos
print(tupla_dos[0]) 
print(tupla_tres[2]) 
print(tupla_cuatro[1]) 
#tupla_dos[0] = "Pablo" # Error
print()

#Otra forma de crear una tupla: empaquetar
nombre= 'Carlos'
apellido= 'Rodriguez'
datos= nombre,apellido,32
print(datos) 
print(type(datos))
print()

#También podemos desempaquetar una tupla para acceder a sus datos
fecha= (7, "noviembre", 2022)
print(fecha)
dd,mm,aa= fecha
print("Dia:",dd)
print("Mes:",mm)
print("Año:",aa)
print()