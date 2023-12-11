# Excepciones múltiples, guardado de los errores
try:
    # n = input("Ingrese un número divisor: ")
    n = float(input("Ingrese un número divisor: "))
    5/n
except TypeError:
    print("No se puede dividir el número entre una cadena") #no se convirtió el tipo de dato
except ValueError:
    print("Debes introducir una cadena que sea un número") #se ingresó una cadena
except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro número") #se ingresó 0
except Exception as e:
    print("Ha ocurrido un error no previsto:", type(e).__name__) #otro error