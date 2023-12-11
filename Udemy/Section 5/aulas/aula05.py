# Atributos de classe
class Pessoa:
    # Atributo para todas as intancias (Caso mude um muda todos)
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

    
p1 = Pessoa(nome='Noki', idade=28)
p2 = Pessoa(nome='Jovem Dex', idade=25)

print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

print()

# Mostra um dicionario do que esta armazenado dentro daquela instancia
print(p2.__dict__)
dicionario = vars(p2)
print(dicionario)