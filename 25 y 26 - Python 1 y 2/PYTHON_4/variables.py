# Ámbito y ciclo de vida de las variables
'''
def saludo(nombre):
    x = 10
    print(f'Hola {nombre}')
saludo('Luis')
# print(x) # NameError: name 'x' is not defined

def muestra_x():
    x = 10
    print(f'x vale {x}')

x = 20
muestra_x() # x vale 10
print(x) #20
'''

y = 20 #Global
def muestra_x():
    x = 10 #Local
    y = 15
    print(f'x vale {x}')
    print(f'y vale {y}')
muestra_x() # x vale 10; y vale 20
print(y)
