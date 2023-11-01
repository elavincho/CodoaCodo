print("****** CADENAS: METODOS ******")

#Join: Unir cadenas
cad = "Pepe Argento"
cad = '_'.join(cad)
print(cad)


#Split: Divide la cadena y arma un vector
cadena = "Cadena de caracteres"
cad_lista = cadena.split(' ')
print(cadena)
print(cad_lista)
print(cad_lista[2])


#Replace
cad = "Programando en JavaScript. JavaScript es lo mejor."
print(cad)
print(cad.replace('JavaScript', 'Python'))
#Quiero reemplazar la 1era vez que aparece la palabra
print(cad.replace('JavaScript', 'Python',1))

#Count e Index
cad = "Cadena de caracteres"
print("Cantidad de c:", cad.count("c"))
print("Primer 'de':", cad.index("de")) #devuelve la posición


#isalpha / isdigit / isalnum
#Devuelve True si son todas letras
cad1 = "Python"
cad2 = "Python3"
print(cad1.isalpha()) 
print(cad2.isalpha())
print()

#Devuelve True si son todos números
cad3 = "1234"
cad4 = "1234a"
print(cad3.isdigit())
print(cad4.isdigit())
print()

#Devuelve True si es Alfanumérico
cad5 = "1234"
cad6 = "Python"
cad7 = ""
cad8 = "12a"
print(cad5.isalnum())
print(cad6.isalnum())
print(cad7.isalnum())
print(cad8.isalnum())
print()


#isupper / islower
cad = "Python"
cad2 = "python"
print(cad.isupper())
print(cad2.islower())


#center / ljust / rjust / zfill
cad = "Python"
cad2 = cad.center(14, "*") #Descuenta la cant de letras de la palabra y rellena el resto con el símbolo
print("Sin centrar:", cad)
print("Centrado:", cad2)

#Ljust: Ajusta a la izquierda
cad2 = cad1.ljust(10,"-")
print(cad2)

#Rjust Ajusta a la derecha
cad2 = cad1.rjust(30,"-")
print(cad2)

#Zfill agrega ceros
num = 345
cad = str(num).zfill(10)
print(cad)


#lstrip / rstrip / strip
#lstrip quita elementos de la izquierda según el caracter que indique
cad = "---Hola Python-izquierda---"
print(cad)
print(cad.lstrip("-"))
print()

#rstrip quita elementos de la derecha
cad2 = "---Hola Python-derecha---"
print(cad2)
print(cad2.rstrip("-"))

#strip quita elementos de ambos lados
cad3 = "---Hola Python---"
print(cad3)
print(cad3.strip("-"))


#find y rfind
cad = "Codo a Codo"
print(cad)
print(cad.find("Codo")) #Devuelve el valor donde encuentra la palabra
print(cad.rfind("Codo")) #Devuelve el valor donde encuentra la palabra desde el final

