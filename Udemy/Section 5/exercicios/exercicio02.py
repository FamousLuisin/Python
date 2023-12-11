# Pilares da poo (abstração, polimofismo, capsulamento e herança)
class Carro:
    def __init__(self, modelo):
        self._fabricante = None
        self.modelo = modelo
        self._motor = None

    @property
    def motor(self):
        return self._motor.tipo

    @motor.setter
    def motor(self, valor):
        self._motor = valor
        
    @property
    def fabricante(self):
        return self._fabricante.nome

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, fabricante, tipo):
        self.fabricante = fabricante
        self.tipo = tipo

class Fabricante:
    def __init__(self, nome):
        self.nome = nome



# Motor
motor = Motor('Volksvagen', 'Turbo')

# Porsche Fabricante
porsche = Fabricante('porsche')

# Porsche Carro
porsche_911 = Carro('911')
porsche_911.fabricante = porsche
porsche_911.motor = motor

print( porsche_911.fabricante, porsche_911.modelo, porsche_911.motor)

