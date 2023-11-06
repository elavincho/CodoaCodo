#Parámetros Opcionales y Posicionales
def registrar_datos(nomcomp, sede="Buenos Aires", anio=2023):
    print(f"Se ha inscripto a {nomcomp.title()} en la sede {sede} para el año {anio}.")


def datos_sede(direccion, ciudad, provincia="Buenos Aires"):
    print(f"Universidad de Python - {direccion} - {ciudad} - {provincia}")




#Programa Principal
#Parámetros opcionales
registrar_datos("agustina gonzález", "Córdoba",2021)
registrar_datos("diego lópez", "Misiones")
registrar_datos("ANA FERNÁNDEZ")

#Parámetros Posicionales
datos_sede("Av. Las Heras 3456", "Godoy Cruz", "Mendoza")
datos_sede(provincia="Chubut", ciudad="Rawson", direccion="Belgrano 321")
datos_sede(ciudad="Mar del Plata", direccion="Av Moreno 56")