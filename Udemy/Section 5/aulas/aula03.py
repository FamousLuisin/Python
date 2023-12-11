# Classes possuem escopo

class Animal:
    def __init__(self, nome):
        self.nome = nome
        print('Classe instanciada')

    def acao(self):
        return f'{self.nome} está atacando'
    
    def executar(self):
        return self.acao()


leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar())