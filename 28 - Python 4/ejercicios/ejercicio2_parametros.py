#funciones_con_parametro
#Parametros: Los vamos a utilizar al definir la funcion
#Argumentos: Las vamos a utilizar al llamar a la funcion


#Funciones
def imprimir_bienvenida(cuat, anio):
    print("Bienvenidos Estudiantes!!")
    print(f"{cuat} cuatrimestre {anio}")

def mostrar_cuotas_curso(importe, fpago):
    fpago = fpago.upper()
    if fpago == "CONTADO":
        print(f"Forma de Pago: Contado. Valor ${importe-(importe*0.1)}")

    elif fpago == "DEBITO" or fpago == "DÉBITO":
        print(f"Forma de Pago: Débito. Valor: ${importe}")

    elif fpago == "CREDITO" or fpago == "CRÉDITO":
        print("Forma de Pago: Crédito.")
        print("Cuotas\tValor Cuota\tTotal Financiado")
        interes = 1.15
        for i in range(3,13,3): #Arrancha en el 3, la ultima cuota es 12 por eso va una mas, y el incremento es de 3 en 3
            valor_cuota = round(importe*(interes)/i,2) #round indica la cantidad de decimales despues de la coma
            total_financiado = valor_cuota*i
            print(f"{i}\t{valor_cuota}\t\t{total_financiado}")
            interes = interes + 0.15

    else:
        print("Forma de Pago Errónea!")



#Programa principal
cuat = input("Escriba un cuatrimestre (1er o 2do): ")
while len(cuat) == 0:
    print("Debe ingresar un cuatrimeste")
    cuat = input("Escriba un cuatrimestre (1er o 2do): ")



anio = int(input("Ingrese un año: "))
while anio < 2000:
    print("Dato no valido, el año debe ser mayor o igual a 2000.")
    anio = int(input("Ingrese un año: "))

imprimir_bienvenida(cuat, anio)



importe = float(input("Ingrese un importe: "))
forma_pago = input("Ingrese una forma de pago (Contado - Débito - Crédito): ")

mostrar_cuotas_curso(importe, forma_pago)
