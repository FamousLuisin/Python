import random
import time

#Classe de ordenação;
class ordenar:
  
  #Função para ordenção apartir da selection sort;
  def selection_sort(self, lista):
    
    #Laço que passará por todos os elemntos da lista;
    for i in range(len(lista)):
    
      #Laço que passará por todos elementos da lista procurando o menor e ordenando;
      for j in range(i+1, len(lista)):
        
        #if que servirá para decidir se o elemntos i da lista é menor ou maior que o elemnto j;
        if lista[j] < lista[i]:
          
          #Se j for menor ele inverterá os valores de i e j na lista;
          lista[i], lista[j] = lista[j], lista[i] 

    return lista
  
  #Definir função bolha (bubbleSort)
  def bolha(self, lista):
    #Definindo o fim da lista
    fim = len(lista)
    """Ao fim da primeira interação coma lista o valor mais"pesada" estará ordenado, 
    logo não será necessario a verificação dele, excluindo-o das proximas interações"""
    for i in range(fim-1, 0, -1):
      for j in range(i):
        if lista[j] > lista[j+1]:
          lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista
  
  def bolha_curta(self, lista):
    #Definindo o fim da lista
    fim = len(lista)
    """Ao fim da primeira interação coma lista o valor mais"pesada" estará ordenado, 
    logo não será necessario a verificação dele, excluindo-o das proximas interações"""
    for i in range(fim-1, 0, -1):
      trocou = False
      for j in range(i):
        if lista[j] > lista[j+1]:
          lista[j], lista[j+1] = lista[j+1], lista[j]
          trocou = True
    
      if not trocou:
        return lista
      
    return lista
  
#Clase para cronometrar
class contaTempos:
  #Função para criar listas;
  def lista_aleatoria(self, n):
    #Criar aleatoria
    lista = [random.randrange(1000) for x in range(n)] 
    return lista
  
  def lista_quase_ordenada(self, n):
    lista = [x for x in range(n)]
    lista[n//2] = -1
    return lista

  
  #Função para cronometrar o tempo;
  def tempo(self, n):
    #Criar uma lista de numero aleatorios;
    lis1 = self. lista_aleatoria(n)
    #Duplicar a lista aleatoria;
    lis2 = lis1[:]
    #criar um objeto ordena na classe ordenar;
    ordena = ordenar()
    
    #Calcular o tempo do bubble sort
    tempoInicial = time.time()
    ordena.bolha(lis1)
    tempoFinal = time.time()
    print("bubble: ", tempoFinal - tempoInicial)
    
    #Calcular o tempo do selection sort
    tempoInicial = time.time()
    ordena.selection_sort(lis2)
    tempoFinal = time.time()
    print("Selection: ", tempoFinal - tempoInicial)

