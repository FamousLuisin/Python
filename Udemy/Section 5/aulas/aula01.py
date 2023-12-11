# Criar classe (Classe é um molde para gerar instancias)
class Pessoa:
    # Todo metodo que seja para tratar de instancias deve ter o self
    # O init é um metodo para inicializar aquela classe e as instancias dela
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

# Criar instancia
p1 = Pessoa('Noki', 'Flinson')
p2 = Pessoa('Maria', 'Pessoa')

print(p1.nome)
print(p2.nome)
