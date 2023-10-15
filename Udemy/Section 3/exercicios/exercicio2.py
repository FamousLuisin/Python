# Exercicio 2

while True:
    primeiro_numero = input("Digite um numero: ")
    operador = input(": ")
    segundo_numero = input("Digite um numero: ")

    # O try nesse caso está sendo usado para não haver uma quebra do programa por causa de algum erro
    # Validação dos numeros
    try:
        primeiro_numero = float(primeiro_numero)
        segundo_numero = float(segundo_numero)
    except:
        print("Um ou ambos dos numeros digitados não é um numero!")
        continue

    #Validação dos operadores    
    if operador not in "+-/*" and len(operador) > 1:
        print("Operação inválida")
        continue

    if operador == "+":
        print(f":{primeiro_numero + segundo_numero}")
    if operador == "-":
        print(f":{primeiro_numero - segundo_numero}")
    if operador == "*":
        print(f":{primeiro_numero * segundo_numero}")
    if operador == "/":
        print(f":{primeiro_numero / segundo_numero}")

    # .lower (deixa tudo em minusculo)
    # .startwith(entrega um boleano baseando se aquela frase começa com determinada letra)
    sair = input("Deseja sair? ").lower().startswith("s")
    print(sair)

    if sair:
        break