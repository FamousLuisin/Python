"""
BubbleSort: Percorre a lista varias vezes, em cada uma verifica o elemento adjacente
e troca de lugar os que estiverem fora de ordem, ao fimda primeira interação com a lista o 
elemento mais "Pesado" estará no fim dessa lista;

548976

{5>4 Sim Inverte
458976
5>8 Não
458976
8>9 Não
458976
9>7 Sim Inverte
458796
9>6 Sim Inverte
458769

FIM PRIMEIRA INTERAÇÃO

4>5 Não
458769
5>8 Não
458769
8>7 Sim Inverte
457869
8>6 Sim Inverte
457689
8>9 Não
457689

FIM SEGUNDA INTERAÇÃO

4>5 Não
457689
5>7 Não
457689
7>6 Sim Inverte
456789}

MEDIR DESEMPENHO EM PYTHON

Mudulo Time
funçaõ time()

import time

antes = time.time()
#algoritmo
depois = time.time()

print("Tempo : ", depois - antes)

BUSCA BINARIA:

é uma busca que vai cortando metade da lista até chegar no que é desejado

"""