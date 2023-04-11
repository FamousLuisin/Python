def computador_escolhe_jogada(n, m):
  jogadaComputador = m

  if m >= n:
    return n
  
  else:
    while jogadaComputador > 0:
      if (n - jogadaComputador) % (m + 1) == 0:
        return jogadaComputador
      jogadaComputador -= 1
  
  return m





def usuario_escolhe_jogada(n, m):
  jogada = int(input("Digite sua jogada: "))
  while jogada < 1 or jogada > m or jogada > n:
    print("Jogada inválida!! Tente novamente")
    jogada = int(input("Digite sua jogada: "))
  
  return jogada





def partida():
  
  #Pedindo dados iniciais
  n = int(input("Digite o numero de peças no tabuleiro: "))
  m = int(input("Digite o maximo de peças a ser retiradas: "))

  vez = False #vez = False, é a vez do computador

  if n % (m + 1) == 0:
    print("Você começa!")
    vez = True #vez = True, é a vez do usuario
  
  else:
    print("Computador começa!")
  

  while n > 0:
    
    if vez:
      jogadaUsuario = usuario_escolhe_jogada(n, m)
      vez = False
      n = n - jogadaUsuario
      print("Você retirou {} peças." .format(jogadaUsuario))
      print("Agora restam {} peças no tabuleiro." .format(n))
    
    else:
      jogadaComputador = computador_escolhe_jogada(n, m)
      vez = True
      n = n - jogadaComputador
      print("O computador tirou {} peça." .format(jogadaComputador))
      print("Agora restam {} peças no tabuleiro." .format(n))
  
  if vez:
    print("Fim do jogo! O computador ganhou!")
  
  else:
    print("Fim do jogo! Você ganhou!")



def campeonato():
  partidas = 1
  vitoriaComputador = 0
  vitoriaUsuario = 0


  while partidas <= 3:
    print("partida {}" .format(partidas))
    if partida():
      vitoriaUsuario += 1
    else:
      vitoriaComputador += 1
    partidas += 1
  
  print("Placar: Você {} X {} Computador" .format(vitoriaUsuario, vitoriaComputador))


def escolha():
  print("1 para partida isolada\n2 para campeonato")
  escolha = int(input("Escolha: "))

  if escolha == 1:
    partida()
  
  else:
    campeonato()



escolha()








