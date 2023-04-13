#Importar função random
import random

#Função para criar listas;
def lista_grande(n):
  lista = []
  #lista = [random.randrange(1000) for x in range n]
  for i in range(n):
    lista.append(random.randint(0, 100))
  
  return lista

print(lista_grande(10))