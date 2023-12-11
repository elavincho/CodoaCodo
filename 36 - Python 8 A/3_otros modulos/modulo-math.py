import math # Importamos el módulo math

# Reondeo
print("Floor:", math.floor(3.99))  # Redondeo a la baja (suelo)
print("Ceil: ", math.ceil(3.01))   # Redondeo al alta (techo)

# Sumatoria mejorada
numeros = [0.9999999, 1, 2, 3]
print("Fsum", math.fsum(numeros)) # 6.9999999

# Truncamiento
print("Trunc", math.trunc(123.45)) # 123

# Potencias y raíces
print("Pow:", math.pow(2, 3))  # Potencia con flotante 
print("Sqrt:", math.sqrt(9))    # Raíz cuadrada (square root)

# Constantes
print("Pi:", math.pi)  # Constante pi
print("E:",math.e)   # Constante e