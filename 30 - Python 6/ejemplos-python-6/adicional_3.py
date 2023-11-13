class Familia:
    def __init__(self, padre, madre, hijos=[]):
        self.padre=padre
        self.madre=madre
        self.hijos=hijos

    # Método especial __str__
    # Python nos permite redefinir el método que se debe ejecutar. Esto se hace definiendo en la clase el método especial __str__
    # Podemos implementar el método __str__ y retornar un string, este luego será el que imprime la función print.
    def __str__(self):
        cadena= f'Padres: {self.padre} y {self.madre}'
        if len(self.hijos)>1:
            cadena = cadena + f'\nHijos: '
            for hijo in self.hijos:
                cadena= cadena + hijo + ", "
        elif len(self.hijos)==1:
            cadena = cadena + f'\nHijo: ' + self.hijos[0]
        else:
            cadena = cadena + f'\nNo tienen hijos'
        return cadena

# Programa principal
familia1=Familia("Juan", "Ana")
familia2=Familia("Pablo", "Noelia", ["Julieta", "Paula"])
familia3=Familia("Fernando", "Luisa", ["Tobías"])
familia4=Familia("Julián", "Daniela", ["Germán", "Leandro", "Florencia"])

print(familia1)
print()
print(familia2)
print()
print(familia3)
print()
print(familia4)
print()