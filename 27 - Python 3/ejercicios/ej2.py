# a) Crear una lista llamada Materias que contendrá 3 materias (harcodeado). Mostrar en pantalla.

materias = ["Python I", "Base de Datos I", "Filosofía"]
print(materias)

# b) Agregar una materia al final y otra en la segunda posición. Mostrar en pantalla la lista, la posición de la primera materia y la posición de la última.

materias.append("Pseudocódigo")
materias.insert(1, "Python II")
print(f"Lista: {materias}")
print(f"Primer Materia: {materias[0]}")
print(f"Última Materia: {materias[len(materias)-1]}")


# c) Solicitar una materia por teclado. Verificar si existe y en caso de que no exista agregarla al final de la lista, recorrer la lista utilizando un bucle for.

mat = input("Ingrese el nombre de la materia: ")
encontrado = False

for i in materias:
    if i.upper() == mat.upper():
        encontrado = True

if encontrado == False:
    materias.append(mat)
    print(f"Materia {mat} agregada con éxito.")
else:
    print(f"No es posible agregar la materia {mat}, ya existe.")

print(materias)


# d) Solicitar una materia por teclado y modificar su nombre por otro ingresado por teclado. Realizar la búsqueda verificando si la materia existe utilizando un bucle while.

mat = input("Ingrese el nombre de la materia a modificar: ")
nuevo_nombre = input("Ingrese el nuevo nombre: ")
encontrado = False
indice = 0
while indice < len(materias) and not encontrado:
    if materias[indice].upper() == mat.upper():
        encontrado = True
        materias[indice] = nuevo_nombre
    indice +=1

if encontrado:
    print(f"Materia {mat} modificada a {nuevo_nombre}.")
else:
    print(f"La materia {mat} no existe en la lista.")


# e) Solicitar una materia por teclado y eliminarla. Realizar la búsqueda verificando si la materia existe utilizando un bucle for - in. Mostrar la lista en pantalla sólo si la materia fue eliminada, junto con un mensaje de confirmación


mat = input("Ingrese el nombre de la materia a eliminar: ")
encontrado = False

for i in materias:
    if i.upper() == mat.upper():
        materias.remove(i)
        encontrado = True

if encontrado:
    print(f"Materia {mat} eliminada.")
    print(f"Lista actualizada de materias: {materias}")
else:
    print(f"La materia {mat} no existe en la lista.")



#f) Eliminar la última materia de la lista y la primera materia de la lista.
# Eliminar la última materia de la lista
if len(materias) > 0:
    ultima_materia = materias.pop()
    print(f"Se eliminó la última materia: {ultima_materia}")
else:
    print("No hay materias en la lista.")

# Eliminar la primera materia de la lista
if len(materias) > 0:
    primer_materia = materias.pop(0)
    print(f"Se eliminó la primer materia: {primer_materia}")
else:
    print("No hay materias en la lista.")