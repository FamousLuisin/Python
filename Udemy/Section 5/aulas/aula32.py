# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass

# Forma de gerar classes mais facil
@dataclass(init=False)
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    # Só pode ser feito se definit init como False
    # Dessa forma aqui, NÃO tem como usar o post_init
    def __init__(self, nome, sobrenome, idade) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self._nome_completo = f'{self.nome} {self.sobrenome}'
        self.idade = idade

    # Método chamado logo depois do "__init__" da dataclasse 
    # NÃO tem como usar o post_init se init=False
    def __post_init__(self):
        print('Usando post init')
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    # Podemos definir métodos
    # property e setters
    @property
    def nome_completo(self):
        return f'{self._nome_completo}'
    
    @nome_completo.setter
    def nome_completo(self, valor):
        # Nome vai apenas pegar o primeiro nome
        # o *sobrenome vai encapsular todo o resto
        nome, *sobrenome = valor.split()
        self.nome = nome
        # Vai pegar cada valor em sobrenome e escrever seprando com espaço
        self.sobrenome = ' '.join(sobrenome)
        self._nome_completo = self.nome + " " + self.sobrenome

if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Flinston',30)
    p2 = Pessoa('Luiz', 'Jhonson', 50)
    print(p1 == p2)

    print(p1.nome_completo)
    p1.nome_completo = 'Noc Flinston Jhonson'
    print(p1.nome_completo)
    print(p1.nome)