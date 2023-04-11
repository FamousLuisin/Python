nome = str(input("Digite o nome: "))
dia = int(input("Digite o dia de vencimento: "))
mes = str(input("Digite o mes de vencimento: "))
valor = str(input("Digite o valor da fatura: "))

print("Olá,", nome)
print("A sua fatura com vencimento em {} de {} no valor de R$ {} está fechada." .format(dia, mes, valor))