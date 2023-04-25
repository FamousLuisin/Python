#Criar uma classe
class Poligono:
    def __init__(self, numero_de_lados):
        self.n = numero_de_lados
        #Criar uma lista com o valor 0 em todos os lados
        self.lados = [0 for i in range(numero_de_lados)]

    def le_lados(self):
        #Funçao para le os lados e colocar na lista
        self.lados = [float(input("Digite o tamanho do lado " + str(i+1) + ": ")) for i in range(self.n)]

    def mostrar_lado(self):
        #Mostrar o valor de todos os lados
        for i in range(self.n):
            print("Lado", i+1, "Tem comprimento de:", self.lados[i])

#Criar subclasse
class Triangulo(Poligono):
    #Construtor da Subclasse
    def __init__(self):
        #Chamar o construtor da superclasse Poligono e dar como parametro numero_de_lados = 3
        Poligono.__init__(self, 3)

    def area(self):
        #Pegar a lista de valor dos lados da classe Mãe e adcionar cada valor em uma variavel
        a, b, c = self.lados
    
        #Calcula o semi-perimetro
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print("area do triangulo é %0.2f" %area)


#Criar subclasse
class Retangulo(Poligono):
    #Construtor da Subclasse
    def __init__(self):
        #Chamar o construtor da superclasse Poligono e dar como parametro numero_de_lados = 4
        Poligono.__init__(self, 4)

    #Sobre escrevendo a função le_lados da superclasse
    def le_lados(self):
        lado1 = float(input("Lado 1: "))
        lado2 = float(input("Lado 2: "))
        self.lados[0] = self.lados[2] = lado1
        self.lados[1] = self.lados[3] = lado2

    #Calcular area
    def area(self):
        return self.lados[0] * self.lados[1]
    
    #calcular diagonal
    def diagonal(self):
        return(self.lados[0]**2 + self.lados[1]**2)**0.5



class TrianguloRetangulo(Triangulo):
    def étrianguloRetangulo(self):
        if (self.lados[0]**2 == self.lados[1]**2 + self.lados[2]**2 or
            self.lados[1]**2 == self.lados[0]**2 + self.lados[2]**2 or
            self.lados[2]**2 == self.lados[1]**2 + self.lados[0]**2):

            return True
        
        else:
            return False
