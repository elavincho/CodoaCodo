#Ejercicios de Python II

#Ingreso de datos

dni = input("Ingrese Su DNI: ")

#validacion isdigit() chequea que una cadena de caracteres sea solo numeros
while not dni.isdigit():
    dni = input("Debe contener solamente numeros. Ingrese su DNI: ")

nombre = input("Ingrese su nombre: ")

#validacion
while len(nombre) > 30:
    nombre = input(f"{nombre} Su nombre es muy largo. Ingrese un nombre mas corto!")

apellido = input("Ingrese su Apellido: ")

#validacion isalpha se utiliza para detectar que sean solo letras
while not apellido.isalpha():
    apellido = input("El apellido no puede contener numeros. Ingrese su Apellido: ")

domicilio = input("Ingrese su Domicilio (Calle + Nro): ")

#validacion

digitos = 0 #Utilizamos una variable auxiliar
for i in domicilio:
    if i.isdigit():
        digitos +=1

while digitos == 0:
    domicilio = input("Debe contener al menos un número. Ingrese su Domicilio (Calle + Nro): ")
    digitos = 0
    for i in domicilio:
        if i.isdigit():
            digitos +=1


#Formato del informe
print()

linea = "="*56
encabezado = " universidad de python - datos del estudiante " # esta escrito a proposito en minusculas
titulo = encabezado.title() #title convierte el texto en mayusculas
titulo_centrado = titulo.center(56, "=") #le indicamos la posicion en la que queremos que nos centre
fecha = "01/11/2023"
fecha = fecha.rjust(56) # r coloca la fecha a la derecha y le indicamos la posicion

print(fecha)
print(linea)
print(titulo_centrado)
print(linea)

usuario = dni.zfill(11) #zfill completa con ceros la cantidad de caracteres que le indicamos
print(f"ID: {usuario}")
print(f"NOMBRE COMPLETO: {apellido.upper()}, {nombre.title()}")
print(f"DOMICILIO: {domicilio.upper()}")
print(f"USUARIO: {apellido.lower()}-{nombre[0].lower()}{dni[:3]}")

nombres = nombre.split(" ") #split hace un corte del espacio, recorre la cadena y cuando encuentre un espacio genera 2 vectores
print(f"CORREO ELECTRONICO: {apellido.lower()}.{nombres[0].lower()}@unipython.com.ar")

print(f"CONTRASEÑA: {apellido.upper()}{nombre[0].lower()}-{dni[-3:]}") #el -3 es para que cuente el vector desde el final

leyenda = '''
Recomendamos cambiar su contraseña.
La presente informacion es confidencial.
Dto. de Sistemas.
'''
print(leyenda)

