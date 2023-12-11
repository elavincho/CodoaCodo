# Propagación de excepciones
'''
Durante la ejecución de un programa, si dentro de una función surge una excepción y la función no la maneja, la excepción se propaga hacia la función que la invocó, si esta otra tampoco la maneja, la excepción continua propagándose hasta llegar a la función inicial del programa y si esta tampoco la maneja se interrumpe la ejecución del programa
'''

def f(x, y):
    return x / y

def g(x, y):
    return f(x, y)

#Programa principal
z = g(5, 0)
print(z) 



'''
# Propagación de excepciones
def funcion(x, y):
  print("antes")
  div = x/y # Excepción!
  print("después")
  return div

def main():
  x = float(input('x: '))
  y = float(input('y: '))
  print(funcion(x, y))
  print("listo")

# Programa principal
main()
'''