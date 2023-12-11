# Módulo datetime
from datetime import datetime

dt = datetime.now()                      # Fecha y hora actual

print("Fecha y hora actual:", dt)       # Imprime fecha y hora actual
print("Año:", dt.year)                  # Año
print("Mes:", dt.month)                 # Mes
print("Dia:", dt.day)                   # Dia

print("Hora:", dt.hour)                 # Hora
print("Minuto:", dt.minute)             # Minuto
print("Segundo:", dt.second)            # Segundo
print("Microsegundo:", dt.microsecond)  # Microsegundo

print()

print(f'Hoy es: {dt.day}/{dt.month}/{dt.year}')
print(f'Hora: {dt.hour}:{dt.minute}:{dt.second}')

print()
dt = datetime(2022,9,28,11,23)
print(dt) #2022-09-28 11:23:00

print()
# dt.year = 3000 # AttributeError: attribute 'year' of 'datetime.date' objects is not writable
dt = dt.replace(year=3000)
print(dt) #3000-09-28 11:23:00