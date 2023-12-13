from dataclasses import dataclass, asdict, astuple

# frozen=True > Não recebe parametros (Deixa a data classe congelada)
# order=True (Não recomendado) > Caso use um sorted ou sort ele ira ordenar a lista
@dataclass()
class Pessoa:
    nome: str
    sobrenome: str
    idade: int = 0 # Podemos fornecer tbm valores padroes (Pórem so os imutaveis)

if __name__ == '__main__':
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    # Recomendado (Permite a fazer a ordenação controlando quais parametros deseja ordenas)
    ordenadas = sorted(lista, reverse=False, key=lambda p: p.sobrenome)
    print(ordenadas)

    print()
    print("====="*12)
    print()

    p1 = Pessoa('Noc', 'Jhonson')
    p2 = Pessoa('Con', 'Nosnohj')
    # Converte para dicionario (Podemos tbm usar os metodos)
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    # Converte para tuple (Podemos tbm usar os metodos)
    print(astuple(p2)[0])
