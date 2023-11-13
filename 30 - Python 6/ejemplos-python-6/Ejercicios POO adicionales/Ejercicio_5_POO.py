# ------------------------- Clase Cliente -------------------------
class Cliente:

    def __init__(self,nombre):
        self.nombre=nombre 
        self.monto=0

    def depositar(self,monto):
        self.monto=self.monto+monto

    def extraer(self,monto):
        self.monto=self.monto-monto

    def retornar_monto(self):
        return self.monto

    def __str__(self):
        return f'{self.nombre}\t $ {self.monto}'

# ------------------------- Clase Banco -------------------------
class Banco:

    def __init__(self, nombre, domicilio):
        self.nombre = nombre
        self.domicilio = domicilio
        self.cliente1=Cliente("Juan")
        self.cliente2=Cliente("Ana")
        self.cliente3=Cliente("Diego")


    def __str__(self):
        return f'{"-"*30}\nBanco {self.nombre} - {self.domicilio}\n{"-"*30}\n'

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)

    def depositos_totales(self):
        print(self.cliente1)
        print(self.cliente2)
        print(self.cliente3)
        print("="*30)
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()
        print(f'Total\t $ {total}')

# ------------------------- Programa principal -------------------------
banco1 = Banco("Santa", "Lavalle 1200")
print(banco1)
banco1.operar()
banco1.depositos_totales()