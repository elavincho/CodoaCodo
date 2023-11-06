#Sintáxis básica

def imprimir_mensaje():
    print("="*38)
    print("Bienvenidos a la Universidad de Python")
    print("="*38)

def imprimir_aulas():
    print("Piso\tAulas")
    for i in range(1,6):
        print(i, end="\t")
        inicio = i*100
        fin = inicio + 10
        print(f"{inicio} a {fin}")

#Programa Principal
imprimir_mensaje()
print()
imprimir_aulas()


