# entrada_teclado.py
def ingreso_entero():
    ''' Tarea: ingresar un número entero '''
    cn = input('Nro entero: ')
    while float(cn) != int(float(cn)):
        cn = input('Nro entero: ')
    return int(cn)

def ingreso_natural():
    ''' Tarea: ingresar un número natural '''
    cn = input('Nro natural: ')
    while float(cn) != int(float(cn)) or int(float(cn)) <= 0 :
        cn = input('Nro natural: ')
    return int(cn)