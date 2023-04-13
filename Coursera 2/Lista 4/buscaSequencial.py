#Criar função de busca;
def busca(lista, elemento):
  #Laço de repetição que irá passar pelos elementos da lista, até achar o que se precisa;
  for i in range(len(lista)):
    #Se encontrar o elemento necessario retornará True  
    if lista[i] == elemento:
      return i
  
  #Se não encontrar o elemento necessario retornará False  
  return False

