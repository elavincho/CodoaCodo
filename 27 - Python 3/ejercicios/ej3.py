# Estadísticas sobre edades de alumnos: 
lista1 = [26,38,47,30,50,19,50,48]
lista2 = [35,40,45,55,21]
edades = lista1 + lista2
print(lista1)
print(lista2)
print(edades)
print(f'Edad más alta: {max(edades)}')
print(f'Edad más baja: {min(edades)}')
print(f'Posición de la edad más baja: {edades.index(min(edades))}')
print(f'Promedio de edades: {sum(edades)/len(edades)}')
print(f'Cantidad de 18 años: {edades.count(18)}')
print(f'Cantidad de 50 años: {edades.count(50)}')
edades.reverse()
print(f'Edades invertidas: {edades}')
edades.sort()
print(f'Edades ordenadas: {edades}')
edades.sort(reverse=True)
print(f'Edades ordenadas al revés: {edades}')
edades.clear()  
print(f'Lista vacía: {edades}')

# Extra: Desempaquetado y pertenencia
turnos = ["Mañana", "Tarde", "Vespertino"]
print(f'Noche está en la lista? {"Noche" in turnos}')
print(f'Mañana está en la lista? {"Mañana" in turnos}')
turno1, turno2, turno3 = turnos
print(turno1)
print(turno2)
print(turno3)