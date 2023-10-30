# groupby - agrupando valores (itertools)
# Agrupar listas ou dicionariso a partir de uma chave
from itertools import groupby

def ordena(aluno):
    return aluno['nota']

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

alunos.sort(key=ordena)
print(*alunos, sep='\n')

grupos = groupby(alunos, key=ordena)

for chave, grupo in grupos:
    print(chave)
    print(*list(grupo), sep='\n')