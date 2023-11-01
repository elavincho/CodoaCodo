#Listas (ejemplos de la presentación)

numeros= [1,2,3,4,5] #Lista de números
dias= ["Lunes", "Martes", "Miércoles"] #Lista de strings
elementos= [] #Lista vacía

sublista= [[1,2,3,],[4,5,6]]

print(numeros)

dias= ["Lunes", "Martes", "Miércoles"]
d1, d2, d3 = dias
print(d1)
print(d2)
print(d3)

lista1= [1,2,3]
lista2= [4,5,6]
lista3= lista1 + lista2
print(lista3) #[1,2,3,4,5,6]

lista=[3,4,5]
# lista= lista + [6] #[3,4,5,6]
lista[1]=7
print(lista) #[3,7,5]

lista=[3,4,5,6]
print(len(lista)) # 4
print(max(lista)) # 6
print(min(lista)) # 3
print(sum(lista)) # 18

lista= list(range(6))
print(lista) #[0,1,2,3,4,5]
print(lista) #[0,1,2,3,4,5]

lista=[3,4,5,6]
print(4 in lista) #True
print(8 in lista) #False

lista=[3,4,5]
lista.append(6)
print(lista) #[3,4,5,6]

lista=[3,4,5]
lista.insert(0,2) #Agrega en la posición 0 el número 2
print(lista) #[2,3,4,5]
lista.insert(3,25) #Agrega en la posición 3 el número 25
print(lista) #[2,3,4,25,5]

lista=[3,4,5]
lista.pop(1) # queda [3,5]

lista=[6,9,8]
lista.pop() # queda [6,9]

lista=[3,4,5]
lista.remove(3) # queda [4,5]

lista=[3,4,5]
print(lista.index(5)) #2

lista=[3,4,5,3,5,8,5]
print(lista.count(5)) #El número 5 está 3 veces
print(lista.count(2)) #El número 2 no está en la lista

lista=[3,4,5]
lista.clear()
print(lista) #[]

lista=[3,4,5]
lista.reverse()
print(lista) #[5,4,3]

lista=[5, 1, 7, 2]
lista.sort()
print(lista) #[1,2,5,7]

lista=[5, 1, 7, 2]
lista.sort(reverse=True)
print(lista) #[7,5,2,1]

#Mostrar la lista, separando los elementos con un espacio
def MostrarLista(lista):
    i = 0
    while i < len(lista):
        print(lista[i], end=" ")
        i = i + 1
    print()

#Declaración de la lista y llamado a la función
lista=["A", "B", "C", "D", "E"]
MostrarLista(lista)

def SumarLista(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    return suma

#Declaración de la lista y llamado a la función
lista=[2,3,4,5,6]
print(SumarLista(lista))

vocales=['a','e','i','o','u']
for i in vocales:
    print(i, end="-")