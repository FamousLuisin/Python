from operator import le
import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    similaridade = 0

    for i in range(len(as_a)):
      similaridade = similaridade + abs(as_a[i] - as_b[i])
    
    return similaridade / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    #Depois criar uma função q junta listas
    
    #Lista senteça OK
    lista_sentesas = separa_sentencas(texto) 
    
    #Lista Frase OK
    lista_frases = [] 
    for sent in range(len(lista_sentesas)):
      
      for frase in separa_frases(lista_sentesas[sent]):
        lista_frases.append(frase)
    
    #Lista Palavra OK
    lista_palavras = [] 
    for frase in range(len(lista_frases)):
      
      for palavra in separa_palavras(lista_frases[frase]):
        lista_palavras.append(palavra)
    
    #tamanho médio de palavras OK
    tamanho_medio_palavras = tamanho_medio_p(lista_palavras)

    #tamanho médio de senteça OK
    tamanho_medio_sentensa = tamanho_medio_s(lista_sentesas)

    #tamanho médio das frases OK
    tamanho_medio_frases = tamanho_medio_f(lista_frases)

    #Complexidade Sentença OK
    complexidade_sentensa = len(lista_frases) / len(lista_sentesas)

    #Palavras diferentes OK
    palavras_diferentes = n_palavras_diferentes(lista_palavras) / len(lista_palavras)

    #Palavras unicas OK
    palavras_unicas = n_palavras_unicas(lista_palavras) / len(lista_palavras) 
    


    return [tamanho_medio_palavras, palavras_diferentes, palavras_unicas, tamanho_medio_sentensa, complexidade_sentensa, tamanho_medio_frases]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    comparados = []
    for texto in textos:
      comparados.append(compara_assinatura(calcula_assinatura(texto), ass_cp))

    menor = comparados[0]
    posisao = 0
    
    for x in range(1, len(comparados)):
      if comparados[x] < menor:
        menor = comparados[x]
        posisao = x

    return posisao + 1

"""
=================================================================================================
=================================================================================================
"""
def tamanho_medio_p(lista_palavras):
    tamanho_medio_palavras = 0
    for palavra in lista_palavras:
      tamanho_medio_palavras = tamanho_medio_palavras + len(palavra)    
    return tamanho_medio_palavras / len(lista_palavras)

def tamanho_medio_s(lista_sentesas):
    tamanho_medio_sentensas = 0
    for sent in lista_sentesas:
      tamanho_medio_sentensas = tamanho_medio_sentensas + len(sent)
    return tamanho_medio_sentensas / len(lista_sentesas)

def tamanho_medio_f(lista_frases):
  tamanho_medio_frases = 0
  for frase in lista_frases:
    tamanho_medio_frases = tamanho_medio_frases + len(frase)
  return tamanho_medio_frases / len(lista_frases)


"""
=================================================================================================
=================================================================================================
"""




def main():
  lista_textos = le_textos()
  assinatura_doente = le_assinatura()
  avalia_textos(lista_textos, assinatura_doente)



print(compara_assinatura([4.34, 0.05, 0.02, 12.81, 2.16, 0.0], [3.96, 0.05, 0.02, 22.22, 3.41, 0.0]))




"""print(calcula_assinatura("Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."))"""
"""print(calcula_assinatura("Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma."))"""
