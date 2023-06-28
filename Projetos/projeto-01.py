import random

while True: 
  # array de palavras
  palavras = ["HAMBURGUER", "PIZZA", "ESFIHA", "STROGONOFF", "PARMEGIANA", "HOTDOG", "TAPIOCA"]

  # numero aleatorio para determinar a palavra escolhida
  sorteio = random.randint(0, len(palavras) - 1)

  # numero de chances que o usuario terá
  vidas = 10

  # palavra que foi escolhida aleatoriamente
  escolhida = palavras[sorteio]

  # lista de letras descobertas
  descobertas = ["_"] * len(escolhida)

  # lista de letras erradas
  erradas = []

  print("---------- FORCA ----------")
  print('\nDICA: COMIDA\n')

  print(" ".join(descobertas), f"\tVIDAS = [{vidas}]", f"\tERRADAS = {erradas}")


  while True:
    # letra digitada pelo usuário
    tentativa = input("\n\nDigite uma letra: ").upper()

    if tentativa in descobertas or tentativa in erradas:
      print('LETRA REPETIDA. TENTE NOVAMENTE:')
      continue


    # verificando se a letra digitada pelo usuário está na palavra
    if tentativa in escolhida:
      print("LETRA CORRETA!!")
      # colocando a letra no lugar correto da palavra
      for i in range(len(escolhida)):
        if escolhida[i] == tentativa:
          descobertas[i] = tentativa
    else: 
      print("LETRA INCORRETA!!")
      vidas -= 1
      # colocando a letra no array de letras erradas
      erradas.append(tentativa)

    # printando a palavra com as letras descobertas
    print(" ".join(descobertas), f"\tVIDAS = [{vidas}]", f"\tERRADAS = {erradas}")

    # se as vidas acabarem, o jogo termina
    if vidas == 0:
      print("\nVOCÊ PERDEU!!")
      print(f"\nA palavra era {escolhida}\n")
      break
    
    # se não existir mais "_" no array, o player venceu
    if "_" not in descobertas:
      print("\nPARABÉNS, VOCÊ ACERTOU A PALAVRA!!")
      print(f"\nA palavra era {escolhida}\n")
      break

  repetir = input('Deseja jogar novamente (s/n): ').upper()

  if repetir == 'S':
    continue
  else:
    print('OBRIGADA POR JOGAR!!')
    print("----------------------------")
    break