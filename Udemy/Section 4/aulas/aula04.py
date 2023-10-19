# x, y, *resto = 1, 2, 3, 4, 5
# print(x, y, resto)

def soma(x, y): # Caso passe mais argumentos que o necessario, nesse caso ele irá quebrar a função (TypeError)
    return x + y

def soma_args(*args): # Nesse caso não há limite de argumentos (argumento se torna uma tupla / empacota os argumentos)
    # args = list(args) # Transformar a tupla de args em uma lista
    soma = 0
    for numero in args:
        soma += numero
    return soma

soma1 = soma_args(10, 20, 30, 40)
print(soma1)

soma2 = soma_args(100, 200, 300, 400, 500)
print(soma2)

tupla_numeros = 1, 2, 3, 4, 5
# Caso queira passar uma variavel  do tipo tupla como argumento, terá que colocar "*" para desempacotar antes
# Terá que desempacotar poís se não ele ira fazer um empacotamento da tupla(tupla dentrod e tupla), dando um erro
soma3 = soma_args(*tupla_numeros) 
print(soma3)

soma_sum = sum((100, 200, 300, 400, 500)) # sum é uma função soma, passando uma tupla como argumentos
print(soma_sum)

