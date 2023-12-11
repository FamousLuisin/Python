# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# Herança: colocar dps da classe filha parenteses
# e dentro a classe pai

# Herança usar no maximo 3 Niveis (classe > classe > classe)
# Tomar cuidado ao usar herança

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_Classe(self):
        print('Classe Pessoa')
        print(self.nome, self.__class__.__name__)

class Aluno(Pessoa):
    ...

class Cliente(Pessoa):
    # Ele sempre procura primeira na classe atual
    # se nn encontrar na classe atual vai para a classe pai
    def falar_nome_Classe(self):
        print('Classe Cliente')
        print(self.nome, self.__class__.__name__)


c1 = Cliente('Nokie', 'Jhonson')
c1.falar_nome_Classe()

a1 = Aluno('Kevin', 'Jhonatan')
a1.falar_nome_Classe()
