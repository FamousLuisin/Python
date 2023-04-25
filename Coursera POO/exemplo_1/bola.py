#Criar classe Bola
class Bola:
    #Variavel da Classe Bola
    conta_bolas = 0

    #Metodo construtor
    def __init__(self, diametro):
        #Variavel de instancia
        self.diametro = diametro
        Bola.conta_bolas +=1