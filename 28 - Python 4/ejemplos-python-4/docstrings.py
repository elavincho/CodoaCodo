def cuad(x):
    """Dado un nro x, calcula x²"""
    return x * x 
def modulo_vector(x, y):
    """Calcula el modulo de un vector 2D.
    Argumentos:
        x: (float|int) coordenada de las abscisas
        y: (float|int) coordenada de las ordenadas
    Devuelve: (float) el modulo del vector
    """
    return (x ** 2 + y ** 2) ** 0.5

print(help(cuad))
print()
print(help(modulo_vector))