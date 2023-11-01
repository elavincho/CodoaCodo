# EJEMPLO: FUNCIÓN QUE DEVUELVE VARIOS VALORES
'''
Tarea: permite recibir un importe y obtiene la mínima cantidad de
billetes a recibir.
Los valores de los billetes pueden ser 500, 100, 50, 20, 10, 5, 1.
'''
def convertir(importe):
    b500 = importe // 500
    importe %= 500
    b100 = importe // 100
    importe %= 100
    b50 = importe // 50
    importe %= 50
    b20 = importe // 20
    importe %= 20
    b10 = importe // 10
    importe %= 10
    b5 = importe // 5
    importe %= 5
    b1 = importe
    return b500, b100, b50, b20, b10, b5, b1

# programa principal
imp = 1626
b500, b100, b50, b20, b10, b5, b1 = convertir(imp)
print(f'b500: {b500}, b100: {b100}, b50: {b50}, b20: {b20}, b10: {b10}, b5: {b5}, b2: {b1}')
