# EJEMPLO: FUNCIÓN QUE DEVUELVE UN VALOR
import math
'''
Ingresar la longitud del radio de una circunferencia.
Calcular y mostrar:
· La superficie del círculo (Sup = pi * r*r)
· El perímetro de la circunferencia (Per = pi * d)
· La superficie de la esfera (Sup = 4 * pi * r*r)
· El volumen de la esfera (Vol = 4/3 * pi * r*r*r)
'''
def calcularSupCirculo(radio):
    '''La superficie del circulo (Sup = pi * r*r)'''
    return math.pi * (radio ** 2)
def calcularPerCircunferencia(radio):
    '''El perímetro de la circunferencia (Per = pi * d)'''
    return math.pi * 2 * radio
def calcularSupEsfera(radio):
    ''' La superficie de la esfera (Sup = 4 * pi * r*r) '''
    return 4 * math.pi * (radio ** 2)
def calcularvolEsfera(radio):
    ''' La superficie de la esfera (Sup = 4 * pi * r*r) '''
    return 4/3 * math.pi * (radio ** 3)

# Programa principal
help(calcularSupCirculo)
radio = float(input('Radio: '))
print(f'Sup. del círculo: {calcularSupCirculo(radio):.2f}')
print(f'Perím. de la circunf.: {calcularPerCircunferencia(radio):.2f}')
print(f'Sup. de la esfera: {calcularSupEsfera(radio):.2f}')
print(f'Vol. de la esfera: {calcularvolEsfera(radio):.2f}')