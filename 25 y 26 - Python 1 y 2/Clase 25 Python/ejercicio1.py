#Triple comilla simple es un bloque de comentarios

# Ejercicio 1: Crear un programa que permita registrar las inscripciones de los alumnos de una universidad privada. Debe incluir un título principal, pedir los datos personales (nombre, edad, fecha de nacimiento). Crear una variable que muestre True o False si posee título secundario (ese dato no se pide al usuario, se escribe en el programa).
# Además se deberá ingresar el monto de matrícula y calcular la cuota (valor de la matrícula + $ 20000 de cuota).
# Finalmente se deberán imprimir todos los datos pedidos.

# en python se la nomenclatura se utiliza snake case
nombre_completo = input("Ingrese su Nombre: ") #string
edad = int(input("Ingrese su Edad: ")) #int (tenemos que convertirlo a entero)
fec_nac = input("Ingrese su Fecha de Nacimiento: ") #string
titulo = True #boolean
matricula = float(input("Ingrese el Monto de la Matricula: ")) #float (tenemos que convertirlo a float)
cuota_mensual = 20000
primer_cuota = matricula + cuota_mensual


#Mostramos los datos
print()
print("=====================================================")
print("===========Universidad de Python=====================")
print("=====================================================")
print()
print("Datos de Ingreso")
print("Nombre completo: ", nombre_completo)
print("Edad: ", edad)
print("Fecha de Nacimiento: ", fec_nac)
print("Titulo: ", titulo)
print("Primer Cuota a Abonar: ", primer_cuota)
print("Valor de Cuotas Restantes: ", cuota_mensual)
