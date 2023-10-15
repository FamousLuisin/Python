import re
import sys
import random

# Pegar o cpf do usuario

# replace troca um elemento especifico por outro
# cpf = input("Digite seu cpf: ").replace(".", "").replace("-", "")

# cpf = input("Digite seu cpf: ")

# # Expressão regular
# cpf = re.sub(
#     r'[^0-9]', # Tudo que não for um numero
#     "", # Substituirá por esse elemento (no caso nada)
#     cpf
# )

# primeiro_caracter = cpf[0]
# repetida = primeiro_caracter * len(cpf) == cpf

# if repetida:
#     print("cpf inválido, caracteres repetidos")
#     sys.exit()



# Gerar CPF automaticamente

cpf = ""

for i in range(9):
    cpf += str(random.randint(0, 9))


# Primeiro digito

nove_digitos = cpf[:9]

contagem_regressiva = 10
valor_regressiva = 0

for numero in nove_digitos:
    valor_regressiva += (int(numero) * contagem_regressiva)
    contagem_regressiva -= 1


primeiro_digito = (valor_regressiva * 10) % 11

if primeiro_digito > 9:
    primeiro_digito = 0



# Segundo digito

dez_digitos = cpf[:10]

contagem_regressiva = 11
valor_regressiva = 0

for numero in dez_digitos:
    valor_regressiva += (int(numero) * contagem_regressiva)
    contagem_regressiva -= 1

segundo_digito = (valor_regressiva * 10) % 11

if segundo_digito > 9:
    segundo_digito = 0



# Criar novo cpf

novo_cpf = f"{nove_digitos}{primeiro_digito}{segundo_digito}"
print(novo_cpf)



# Validar um cpf entrege pelo usuario

# if cpf == novo_cpf:
#     print(cpf, "cpf válido")

# else:
#     print("cpf inválido")