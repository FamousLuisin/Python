# def define uma funçao, que pode ou não receber parametros (nome das variaveis da função)
# Os parametros de uma funçao caso não nenha um valor inicial devem ser passados, caso contrario dará ERRO
# Argumentos são os valores entregues para a funçao
# Se colocar um valor padrão em um parametro, tem q se atentar que todos os parametros após ele tbm terá que ter valor

def soma(x, y, z=None): # x e y são parametros, z é um parametro None
    
    if z is not None: # Nessa caso dará para saber se z for enviado, pois o valor dele irá para de ser None
        print(f"{x=} + y={y} + {z=}", "|", "x + y + z =",  x + y + z)
    else:
        print(f"{x=} {y=}", "|", "x + y =", x + y)

soma(1, 2, 3) # Arguemnto não nomeado
# os argumentos de uma função sempre recebe os valores em ordem, se quiser por exemplo trocar essa ordem usa os:
soma(y=2, z=3, x=1) # Argumentos nomeados (se passar um nomeado todos os outros a frente tbm teram q ser nomeados)
soma(5, 5)



def saudacao(nome="Sem nome"):
    print(f"Olá, {nome}")

saudacao("Flinston")
saudacao()

