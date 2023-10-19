x = 1

def escopo():
    # (NÃO USAR GLOBAL) Global, faz com que uma variavel do escopo externo seja manipulada por um escopo interno
    # global x # Definir "x" como global, nesse caso o "x" externo da função é o mesmo de dentro da função escopo()
    x = 10
    def segundo_escopo():
        x = 20 # Esse "x" por nn ser definido global pertence somente a função segundo_escopo
        y = 2 # Esse "y" é só do escopo da função segundo_escopo()
        print(x, y)
    
    segundo_escopo()
    print(x)

print(x)
escopo()
print(x)