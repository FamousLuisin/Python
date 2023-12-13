from typing import Union, Optional
import contas

class Pessoa():
    
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return f'Nome: {self._nome}'
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome
        print(f'Nome alterado para {nome}')
    
    @property
    def idade(self):
        return f'Idade: {self._idade}'
    
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade
        print(f'Idade redefinida para {idade}')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        atributos = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{atributos}'
        


class Cliente(Pessoa):
    
    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade)
        self.conta = None

    def adicionar_conta(self, conta):
        self.conta = conta



if __name__ == "__main__":
    p1 = Cliente('Noki', 28)
    print(p1)
    p2 = Cliente("Mike", 26)
    print(p1 == p2)
    
    print()
    print("=#="*20)
    print()

    c1 = contas.ContaPoupanca(666, 777, 10)
    c2 = contas.ContaPoupanca(777, 666, 1)
    p1.adicionar_conta(c1)
    p2.adicionar_conta(c2)
    print(p1.conta == p2.conta)
    print(p1.conta)

