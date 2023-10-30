import sys
sys.setrecursionlimit(1002)

def fatorial(x):
    if x <= 1:
        return x
    
    return x * fatorial(x - 1) # função recursiva é uma função que se chama

# se não colocar um limite (caso base) ele da erro de stackover flow (RecursionError)
def recursiva(inicio=0, fim=10):
    if inicio >= fim:
        return fim
    # Caso recursivo
    # Contar até chegar ao fim
    print(inicio)
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva(0, 1000))