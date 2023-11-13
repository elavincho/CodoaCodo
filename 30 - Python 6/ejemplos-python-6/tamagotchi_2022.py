class Tamagotchi:
    nombre = ""
    hambre = 0
    animo = 0
    energia = 0

    def __init__(self,nombre,hambre,animo,energia):
        self.nombre = nombre
        self.hambre = hambre
        self.animo = animo
        self.energia = energia
                
    def jugar(self):
        self.animo+=1
        self.energia-=1

    def alimentar(self):
        self.animo+=1
        self.hambre-=1

    def dormir(self):
        self.hambre+=1
        self.energia+=1

    def pasar(self):
        self.animo-=1
        self.hambre+=1
        self.energia-=1
      
    def __str__(self):
       cadena = f'Nombre: {self.nombre} \nHambre: {self.hambre} | Animo: {self.animo} | Energia: {self.energia}'
       return cadena

# Programa Principal
t=Tamagotchi("Tamagotchito",10,10,10)
print(t)
op= int(input("Seleccione qué desea hacer: \n1: Dormir\n2: Jugar\n3: Alimentar\n4: Pasar el tiempo\n0: Salir\nIngrese su opción: "))
while op!=0:
    if op == 1:
        t.dormir()
    elif op == 2:
        t.jugar()
    elif op == 3:
        t.alimentar()
    elif op == 4:
        t.pasar()
    else:
        print("Opción incorrecta:")
    print(t)
    op= int(input("Seleccione qué desea hacer: \n1: Dormir\n2: Jugar\n3: Alimentar\n4: Pasar el tiempo\n0: Salir\nIngrese su opción: "))

'''
TO-DO:
- Topear a 10 los valores
- No permitir jugar si tiene hambre o está cansado
- Mejorar salida (menú)
'''
