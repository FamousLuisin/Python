from abc import abstractmethod, ABC

class Conta(ABC):
    
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def deposito(self, valor: float):
        self.saldo += valor
        self.detalhes(f'(DEPOSITO {valor:.2f})')
        return self.saldo
    
    def detalhes(self, msg: str = ''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('---')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        atributos = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{atributos}'

    @abstractmethod
    def saque(self, valor: float) -> float:...


class ContaCorrente(Conta):

    tipo = 'Corrente'

    def __init__(self, agencia: int, conta: int, saldo: float, limite: int = 1200) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite
        
    def saque(self, valor):
        if valor <= self.limite + self.saldo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor:.2f})')
            return self.saldo
        
        print('Valor desejado fora do limite')
        self.detalhes(f'(SAQUE NEGADO {valor:.2f}) | (LIMITE {self.saldo + self.limite:.2f})')
        return self.saldo
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        atributos = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{atributos}'
    
    
class ContaPoupanca(Conta):

    tipo = 'Poupança'

    def __init__(self, agencia, conta, saldo) -> None:
        super().__init__(agencia, conta, saldo)

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor:.2f})')
            return self.saldo
        
        print('Valor desejado fora do limite')
        self.detalhes(f'(SAQUE NEGADO {valor:.2f})')
        return self.saldo

        


if __name__ == '__main__':
    contaP = ContaPoupanca(0, 0, 0)
    contaP.saque(1200)
    contaP.saque(1)
    contaP.deposito(2200)
    contaP.saque(500)

    print()
    print("#####"*12)
    print()

    contaC = ContaCorrente(0, 0, 0)
    contaC.saque(1200)
    contaC.saque(1)
    contaC.deposito(2200)
    contaC.saque(500)




    