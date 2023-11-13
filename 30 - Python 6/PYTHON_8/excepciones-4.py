# Propagación de excepciones
def funcion(x, y):
  print("antes")
  div = x/y
  print("después")
  return div

def main():
  x = float(input('x: '))
  y = float(input('y: '))
  try:
    print(funcion(x, y))
  except:
    print("Algo salió mal")
  print("listo")

main()
