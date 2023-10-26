# try sempre precisa de outro bloco

try:
    print('ABRIR AQRQUIVO')
    print(10 / 1)
except ZeroDivisionError:
    print('Dividiu zero')
else: # O else acontece quando não tiver nenhum erro / excessao
    print('sem erros')
finally: # finally sempre é executado mesmo com erro ou sem erro
    print('FECHAR ARQUIVO')