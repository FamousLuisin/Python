# Criar função que recebe um argumento (numero) e verifica se ele é par ou impar

def par_impar(numero):
    
    if numero % 2 == 0:
        return "Par"
    
    return "Impar"


print(par_impar(10))
print(par_impar(11))