# Criar varios multiplicadores usando clousure

def multiplicar(multiplciador):
    
    def calcular(numero):
        return f"{numero} * {multiplciador} = {numero * multiplciador}"
    
    return calcular

duplicar = multiplicar(2)
triplicar = multiplicar(3)
quadruplicar = multiplicar(4)

print(f"duplicar = {duplicar(5)}\ntriplicar = {triplicar(5)}\nquadruplicar = {quadruplicar(5)}")