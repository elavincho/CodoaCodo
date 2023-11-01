#Ingreso de Datos
dni = input("Ingrese su DNI: ")
#Validación
while not dni.isdigit():
    dni = input("Debe contener solamente número. Ingrese su DNI: ")


nombre = input("Ingrese su nombre: ")
#validación
while len(nombre) > 30:
    nombre = input(f"{nombre} su nombre es muy largo. Ingrese un nombre más corto: ")

apellido = input("Ingrese su apellido: ")
#validación
while not apellido.isalpha():
    apellido = input("El apellido contiene números. Ingrese su apellido: ")

domicilio = input("Ingrese su domicilio (Calle + Número): ")
#Validación

digitos = 0
for i in domicilio:
    if i.isdigit():
        digitos +=1

while digitos == 0:
    domicilio = input("Debe contener al menos un número. Ingrese su domicilio (Calle + Número): ")
    digitos = 0
    for i in domicilio:
        if i.isdigit():
            digitos +=1

#Formato del informe
linea = "="*56
encabezado = " universidad de python - datos del estudiante "
titulo = encabezado.title()
titulo_centrado = titulo.center(56, "=")
fecha = "01/11/2023"
fecha = fecha.rjust(56)

print(fecha)
print(linea)
print(titulo_centrado)
print(linea)

usuario = dni.zfill(11)
print(f"ID: {usuario}")
print(f"NOMBRE COMPLETO: {apellido.upper()}, {nombre.title()}")
print(f"DOMICILIO: {domicilio.upper()}")
print(f"USUARIO: {apellido.lower()}-{nombre[0].lower()}{dni[:3]}")

nombres = nombre.split(" ")
print(f"CORREO ELECTRÓNICO: {apellido.lower()}.{nombres[0].lower()}@unipython.com.ar")

print(f"CONTRASEÑA: {apellido[0].upper()}{nombre[0].lower()}-{dni[-3:]}")


leyenda = '''
Recomendamos cambiar su contraseña.
La presente información es confidencial.
Dpto. de Sistemas 
'''
print(leyenda)