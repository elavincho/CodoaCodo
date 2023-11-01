print("****** CONJUNTOS ******")

#Creación de conjuntos
conj_uno = set()
conj_dos = {'Juan','Juan'}
conj_tres = {'Pablo', 3456, True}
conj_cuatro = {'Rivadavia', 3567, ('Calle 1', 'Calle2')}

print("Conjunto vacío:",conj_uno)
print("Conjunto str:",conj_dos)
print("Conjunto combinado:",conj_tres)
print("Conjunto combinado:",conj_cuatro)
print("")

print("Iteración de elementos:")
#Acceso a elementos
conj_cinco = {1,2,5,6,9}
for i in conj_cinco:
    print(i, end=' ')
print()