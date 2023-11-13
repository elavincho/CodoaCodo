#Getters y Setters
# Más info en: https://www.freecodecamp.org/espanol/news/python-decorador-property/#:~:text=Una%20funci%C3%B3n%20decoradora%20(%22decorator%20function,una%20funci%C3%B3n%20existente%20sin%20modificarla.

class Color:

    def __init__(self):
        self.__color = 'Azul' #Atributo de instancia privado

    @property #Getter
    def favorito(self):
        return f'Mi color favorito es: {self.__color}'

    @favorito.setter
    def favorito(self, color):
        self.__color = color

color1 = Color()
print(color1.favorito)
color1.favorito = 'Rojo'
print(color1.favorito)