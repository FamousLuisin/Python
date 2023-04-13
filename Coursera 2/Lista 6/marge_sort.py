#Definir função marge sort;
def marge_sort(lista):
  
  #BASE RECURSÃO;
  if len(lista) <= 1:
    return lista
  
  #meio da lista;
  meio = len(lista) // 2

  #Divisão da lista até varias listas contendo apenas um elemento;
  lado_esquerdo = marge_sort(lista[:meio])
  lado_direito = marge_sort(lista[meio:])

  #ordenação par a par de listas, partindo da ordenação de listas com um elemento;
  return marge(lado_esquerdo, lado_direito)



def marge(lado_esquerdo, lado_direito):
  if not lado_esquerdo: #Se não existir lado esquerdo;
    return lado_direito
  
  if not lado_direito:  #Se não existir um lado esquerdo;
    return lado_esquerdo
  
  #ordenção da lista, retornando o menor elemento entre as listas e refazendo o marge do que sobrar da lista esquerda e direita;
  if lado_direito[0] > lado_esquerdo[0]:
    return [lado_esquerdo[0], marge(lado_esquerdo[1:], lado_direito)]
  
  else:
    return [lado_direito[0], marge(lado_esquerdo, lado_direito[1:])]



