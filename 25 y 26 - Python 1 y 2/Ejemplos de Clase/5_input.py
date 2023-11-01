#Ingresar datos con input
variable= input() #retorna un string
print("Hola", variable)


variable= input("Ingrese su nombre: ") #retorna un string
print("Hola", variable)


mensaje = "Bienvenido al sistema. Ingrese su usuario: "
usuario= input(mensaje) 
print("Hola", usuario)


anio = input("Ingrese el año actual: ")
print("El año próximo será: ", anio + 1)

#Debo castear el ingreso del input para poder realizar la suma
anio = int(input("Ingrese el año actual: "))
print("El año próximo será: ", anio + 1)




#Otro ejemplo
lado = input("Ingresar el lado del cuadrado: ")
superficie = lado*lado
print(superficie)



lado = int(input("Ingresar el lado del cuadrado: "))
superficie = lado*lado
print("La superficie es: "+ superficie) #Error
print("La superficie es: "+ str(superficie))
print("La superficie es:", superficie) #Otra forma para combinar string con int
