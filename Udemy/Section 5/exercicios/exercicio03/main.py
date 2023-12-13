from clientes import Cliente
from contas import ContaCorrente, ContaPoupanca
from banco import Banco

p1 = Cliente('Noki', 28)
c1 = ContaPoupanca(666, 777, 10)
p1.adicionar_conta(c1)

p2 = Cliente("Mike", 26)
c2 = ContaCorrente(555, 666, 1)
p2.adicionar_conta(c2)

banco = Banco('Jhonson')
banco.adcionar_agencia(666)
banco.adcionar_agencia(777)
banco.adcionar_agencia(555)


banco.adcionar_cliente(p1)
banco.adcionar_conta(c1)

banco.adcionar_cliente(p2)
banco.adcionar_conta(c2)

if banco.auth(p2, c2):
    c2.deposito(10)
    p2.conta.deposito(100)