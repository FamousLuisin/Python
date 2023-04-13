"""
================================================================================================================

busca sequencial: metodo de buscar um elemento dentro de uma lista com x elementos;

def busca(lista, elemento):
  for i in range(len(lista)):
    if lista[i] == elemento:
      return True
    
    retturn False

================================================================================================================

Complexidade computacional: 
  -Analise matematica do desempenho de um algoritmo
  -Estudo analitico, para ver:
    >Quantas operações são necessarias para executar o algoritmo;
    >Quanto tempo ele vai demorar para ser executado;
    >Quanta memória ele vai ocupar;
  -Busca sequencial de n elementos:
    >Melhor caso (1);
    >Pior caso(n);
    >caso médio(n/2);
    >Vantagens: (Simples, Funciona bem com volumes pequenos de dados);
    >Desvantagens: (Alta complexidade computacional, Muita lenta com grandes volumes de dados);

================================================================================================================

Algoritmos de ordenação(Seleção direta > Selection Sort);
  -Primeiro passo é buscar o menor elemento da lista e coloca-lo no inicio;
  -Após o primeiro passo pegar os menores elementos subsequentes ainda nn ordenados, e colocar em ordem;


"""