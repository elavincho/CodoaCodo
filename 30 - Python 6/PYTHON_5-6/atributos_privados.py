# class Ejemplo:
#     __atributo_privado = "Soy un atributo inalcanzable desde fuera."
# e = Ejemplo()
# print(e.__atributo_privado)

# class Ejemplo:
#     def __metodo_privado(self):
#         print("Soy un método inalcanzable desde fuera.")
# e = Ejemplo()
# e.__metodo_privado()

class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."

    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera.")

    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado()

e = Ejemplo()
print(e.atributo_publico())
e.metodo_publico()