#Pasaje por valor
def doblar_valor(numero):
    numero *= 2

n = 10
doblar_valor(n)
print(n) #10, no afecta a la variable, sigue valiendo lo mismo
def doblar_valor(numero):
    return numero * 2

n = 10
n = doblar_valor(n)
print(n) #20


#Pasaje por referencia
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns = [10,50,100]
doblar_valores(ns)
print(ns) #[20, 100, 200]

ns = [10,50,100]
doblar_valores(ns[:])  # Una copia al vuelo de una lista con [:]
print(ns) #[10, 50, 100]