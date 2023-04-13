import ordenar
import random
import time


#Clase para cronometrar
class contaTempos_Import:
  #Função para criar listas;
  def lista_aleatoria(self, n):
    #Criar lista vazia
    lista = []
    #adicionar n numeros aleatorio a lista vazia;
    for i in range(n):
      #random.randit(0, 100), gera um numero aleatorio inteiro entre 0 e 100;
      lista.append(random.randint(0, 100))
  
    return lista
  
  def lista_quase_ordenada(self, n):
    lista = [x for x in range(n)]
    lista[n//10] = -1
    return lista
  

  #Função para cronometrar o tempo;
  def tempo(self, n):
    #Criar uma lista de numero aleatorios;
    lis1 = self.lista_aleatoria(n)
    #Duplicar a lista aleatoria;
    lis2 = lis1[:]
    lis3 = lis1[:]
    lis4 = lis1[:]
    #criar um objeto ordena na classe ordenar;
    ordena = ordenar.ordena()
    
    #Calcular o tempo do bubble sort
    tempoInicial = time.time()
    ordena.bubble_sort(lis1)
    tempoFinal = time.time()
    print("bubble: ", tempoFinal - tempoInicial)
    
    #Calcular o tempo do bubble sort curto
    tempoInicial = time.time()
    ordena.bubble_curta(lis2)
    tempoFinal = time.time()
    print("bubble curto: ", tempoFinal - tempoInicial)
    
    #Calcular o tempo do selection sort
    tempoInicial = time.time()
    ordena.selection_sort(lis3)
    tempoFinal = time.time()
    print("Selection: ", tempoFinal - tempoInicial)
    
    #Calcular o tempo do selection sort
    tempoInicial = time.time()
    ordena.insertion_sort(lis4)
    tempoFinal = time.time()
    print("insertion: ", tempoFinal - tempoInicial)

o = contaTempos_Import()
o.tempo(1000)
