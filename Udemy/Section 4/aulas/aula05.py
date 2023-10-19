# higher order function ou funções de primeira classe
# Higher Order Functions - Funções que podem receber e/ou retornar outras funções
# First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

def saudacoes(msg, nome):
    return f"{msg}, {nome}"

def executar(funcao, *args):
    return funcao(*args) #da para chamar uma função dentro de uma funçao

 # Da para passar uma função (no caso o nome dela) como argumento, para ser ultilizado posteriormente
variavel = executar(saudacoes, "Bom dia", "Luis", "yamete")
print(variavel)
