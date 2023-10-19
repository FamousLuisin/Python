def soma (x, y):
    if x >= 20:
        return 10, 20 # Esse é um return de tuple
    return x + y # Retornar um valor

soma1 = soma(1, 2)
soma2 = soma(3, 4)
soma3 = soma(soma1, soma2)
print(soma1, "|", soma2, "|", soma3)

print(soma(100, 10), type(soma(100, 10)))