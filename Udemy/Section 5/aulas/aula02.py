# classe = Objeto / Molde
# atributos = Valores / Dados do objeto;
# Métodos = Ações
class Carro:
    def __init__(self, nome='Sem nome'):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')

carro = Carro('Fusca')
print(carro.nome)

carro2 = Carro('Celta')
print(carro2.nome)

carro.acelerar()
Carro.acelerar(carro2)
