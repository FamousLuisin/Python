# Metodos de classe e fabricas
class Pessoa:
    ano_atual = 2023 # Atributo classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Metodo de instancia
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
    # Metodo de classe
    # Decorar um metodo e precisa receber a classe (o Molde)
    @classmethod
    def metodo_classe(cls):
        print('Hey')

    # Metodo para criar Pessoas
    @classmethod
    def criar_pessoa(cls, nome, idade):
        return cls(nome, idade)
    
    # Metodo para criar Pessoas Anonimas
    @classmethod
    def criar_pessoa_anonima(cls, idade):
        return cls('Anonimo', idade)
    
    # Função dentro da classe que não tem acesso ao self e nem ao cls
    @staticmethod
    def saudacao():
        print("Metodo statico: Salve")

    
p1 = Pessoa(nome='Noki', idade=28)
p2 = Pessoa(nome='Jovem Dex', idade=25)

p3 = Pessoa.criar_pessoa('Mike', 22)
p4 = Pessoa.criar_pessoa_anonima(30)

print("Sem metodo:", p2.nome)
print("Metodo criar_pessoa:", p3.nome)
print("Metodo criar_pessoa_anonima:", p4.nome)

Pessoa.saudacao()