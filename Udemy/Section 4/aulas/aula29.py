a = 18
b = 1

# Silenciar o erro (Tudo que vier depois tbm é silenciado)
# silencia inclusive outros erros, ou pode até mesmo tratar erros de uma maneira errada
try:
   print('linha'[100])
   c = a / b
   print('linha')
# Tratar os erros de ZeroDivisionError
except ZeroDivisionError: # Excessões são classes
    print("Divisão por 0")
# Tratar os erros de NameError
except NameError:
    print("algum elemento não definido")
except (TypeError, IndexError) as error: # o erro é uma variavel nesse caso para pegar o erro ocorrido
    print("Problema de tipo ou index")
    print('msg:', error) # mensagem da excessao
    print('nome:', error.__class__.__name__)  # nome da excessao
# Tratar qualquer erro existente
except Exception: 
    print("ERRO DESCONHECIDO")

print("FIM")