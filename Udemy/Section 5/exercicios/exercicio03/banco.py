import clientes
import contas

class Banco():
    
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self._clientes = []
        self._contas = []
        self._agencias = []

    def auth(self, cliente: clientes.Cliente, conta: contas.Conta):
        if cliente in self._clientes and conta in self._contas and conta.agencia in self._agencias:
            if cliente.conta is conta:
                return True
            print('cliente errado')
            return False
        print('Ha alguma informação errada')
        return False
    
    def adcionar_cliente(self, cliente: clientes.Pessoa):
        self._clientes.append(cliente)

    def adcionar_conta(self, conta: contas.Conta):
        self._contas.append(conta)

    def adcionar_agencia(self, agencia: int):
        self._agencias.append(agencia)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        atributos = f'({self.nome!r}, {self._agencias!r}, {self._clientes!r}, {self._contas!r})'
        return f'{class_name}{atributos}'
    
if __name__ == "__main__":
    p1 = clientes.Cliente('Noki', 28)
    c1 = contas.ContaPoupanca(666, 777, 10)
    p1.adicionar_conta(c1)

    p2 = clientes.Cliente("Mike", 26)
    c2 = contas.ContaPoupanca(777, 666, 1)
    p2.adicionar_conta(c2)

    banco = Banco('Jhonson')
    banco.adcionar_cliente(p1)
    banco.adcionar_conta(c1)

    banco.adcionar_cliente(p2)

    if banco.auth(p1, c1):
        c1.deposito(10)
        p1.conta.deposito(100)