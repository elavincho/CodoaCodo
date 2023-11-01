#a Crear una lista llamada Materias que contendrá 3 materias (harcodeado). Mostrar en
#pantalla.

materias = ["Python I", "Base de Datos I", "Filosofía"]
print(materias)


#b

materias.append("Pseudocódigo") #append agrega un elemento en la ultima posicion
materias.insert(1, "Python II") #insert agrega elementos en la 

print(f"Lista: {materias}")
print(f"Primer Materia: {materias[0]}")
print(f"Última Materia: {materias[len(materias)-1]}")

#C

mat = input("Ingrese el nombre de la materia: ")

encontrado = False
for i in materias:
    if i.upper() == mat.upper():
        encontrado = True

if encontrado == False:
    materias.append(mat)
    print(f"Materia {mat} agregada con exito")
else:
    print(f"No se puede agregar la materia {mat} ya existe!")
    
print(materias)

#d

mat = input("Ingrese el nombre de la materia a modificar: ")
nuevo_nombre = input("Ingrese el nuevo nombre de la materia: ")

encontrado = False
indice = 0
while indice < len(materias) and not encontrado:
    if materias[indice].upper() == mat.upper():
        encontrado = True
        materias[indice] = nuevo_nombre
    indice += 1
if encontrado:
    print(f"Materia {mat} modificada a {nuevo_nombre}.")
else:
    print(f"La materia {mat} no existe en la lista!")


#e

mat = input("Ingrese el nombre de la materia a eliminar: ")
encontrado = False

for i in materias:
    if i.upper() == mat.upper():
        materias.remove(i)
        encontrado = True
if encontrado == True:
    print(f"Materia {mat} fue eliminada!")
    print(f"Lista actualizada de materias: {materias}")
else:
    print(f"La materia no existe en la lista!")

#f
#Eliminar la ultima materia de la lista
if len(materias) > 0:
    ultima_materia = materias.pop()
    print(f"Se elimino la ultima materia: {ultima_materia}")
else:
    print(f"No hay materias en la lista!")



#Eliminar la primer materia de la lista
if len(materias) > 0:
    primer_materia = materias.pop(0)
    print(f"Se elimino la primera materia: {primer_materia}")
else:
    print(f"No hay materias en la lista!")






