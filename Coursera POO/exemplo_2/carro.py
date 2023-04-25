#Criar classe carro
class Carro:
    #construtor da classe
    def __init__(self, modelo, ano, cor, velocidadeMaxima):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        self.velocidadeMaxima = velocidadeMaxima

    def imprima(self):
        if self.velocidade == 0:
            print("%s %s %d" %(self.modelo, self.cor, self.ano))

        elif self.velocidade < self.velocidadeMaxima:
            print("{} {} {}".format(self.modelo, self.cor, self.velocidade))

        else:
            print("%s %s %d RAPIDO" %(self.modelo, self.cor, self.velocidade))

    def acelere(self, velocidade):
        self.velocidade = velocidade
        if self.velocidade > self.velocidadeMaxima:
            self.velocidade = self.velocidadeMaxima
        self.imprima()

    def pare(self):
        self.velocidade = 0
        self.imprima()


fordPica = Carro("Mustang", 1995, "preto", 200)
fordPica.acelere(150)
fordPica.acelere(100)
fordPica.acelere(200)
fordPica.pare()