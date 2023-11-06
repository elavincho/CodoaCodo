#Funciones con Parámetros
#Parámetros: Al definir la función
#Argumentos: Al llamar a la función

#funciones
def imprimir_bienvenida(cuat, anio):
    print("Bienvenidos estudiantes!")
    print(f"{cuat} cuatrimestre {anio}")

def mostrar_cuotas_curso(importe, fpago):
    fpago = fpago.upper()
    if fpago == "CONTADO":
        print(f"Forma de pago: Contado. Valor {importe-(importe*0.1)}")

    elif fpago == "DEBITO" or fpago == "DÉBITO":
        print(f"Forma de Pago: Débito. Valor: {importe}")

    elif fpago == "CREDITO" or fpago =="CRÉDITO":
        print("Forma de Pago: Crédito.")
        print("Cuotas\tValor Cuota\tTotal Financiado")

        interes = 1.15
        for i in range(3,13,3):  
            valor_cuota = round(importe*(interes)/i,2)
            total_financiado = valor_cuota * i
            print(f"{i}\t{valor_cuota}\t\t{total_financiado}")
            interes = interes + 0.15
    else:
        print("Forma de pago errónea.")



#Programa Principal
cuat = input("Escriba un cuatrimestre (1er o 2do): ")
while len(cuat) == 0:
    print("Debes escribir un valor.")
    cuat = input("Escriba un cuatrimestre (1er o 2do): ")



anio = int(input("Ingrese el año: "))
while anio < 2000:
    print("Dato no válido, debe ser mayor o igual a 2000.")
    anio = int(input("Ingrese el año: "))


imprimir_bienvenida(cuat, anio)

importe = float(input("Ingrese un importe: "))
forma_pago = input("Ingrese una forma de pago (Contado/Débito/Crédito): ")
mostrar_cuotas_curso(importe, forma_pago)