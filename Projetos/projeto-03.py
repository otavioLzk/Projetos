""" Projeto: Adivinhe o número
Descrição: Neste jogo, o programa escolhe aleatoriamente um número entre 1 e 100. O jogador deve tentar adivinhar o número correto dentro de um número limitado de tentativas.
Regras:
O programa escolhe um número aleatório entre 1 e 100.
O jogador tem no máximo 10 tentativas.
O jogador faz uma suposição fornecendo um número.
O programa informa ao jogador se o número correto é maior ou menor do que a suposição feita.
O jogador continua fazendo suposições até adivinhar corretamente o número ou esgotar o número de tentativas.
Funcionalidades adicionais:
No início do jogo, o programa exibe uma mensagem de boas-vindas e explica as regras do jogo.
O programa mantém um registro do número de tentativas do jogador.
Ao final do jogo, o programa informa se o jogador adivinhou corretamente o número ou não, e exibe o número de tentativas realizadas.
O programa pergunta se o jogador deseja jogar novamente.
Dicas:
Você pode usar a biblioteca random em Python para gerar o número aleatório.
Utilize estruturas de controle como loops e condicionais para implementar a lógica do jogo.
Lembre-se de validar a entrada do jogador, garantindo que seja um número dentro do intervalo correto. """

import random

print('\n' + ('*'*50))
print('Seja bem vindo!!')
print('As regras do jogo são: \n * O sistema irá gerar um número aleatório entre 1 e 100. \n * O objetivo do jogo é acertar o número sorteado. \n * O usuário terá 10 tentativas. \n * A cada rodada, o sistema informará ao usuário se a \ntentativa feita é menor ou maior do que o número sorteado.')
print(('*'*50) + '\n')


while True:
    sorteio = random.randint(1, 100)
    tentativas = 10

    while True:
        if tentativas == 0:
            print('SUAS TENTATIVAS ACABARAM!!')
            print(f'O número sorteado era {sorteio} =) ')
            break

        jogada = int(input('Digite um número entre 1 e 100: '))

        if jogada < 1 or jogada > 100:
            print('Número inválido, tente novamente!!\n')
            continue

        if sorteio == jogada:
            tentativas-=1
            print(f'\nPARABÉNS, VOCÊ ACERTOU EM {10-tentativas} TENTATIVAS!!!\n')
            break

        if sorteio > jogada:
            print('O número sorteado é maior!\n')
            tentativas-=1
            continue
        else:
            print('O número sorteado é menor!\n')
            tentativas-=1
            continue
    
    repetir = input('Deseja jogar novamente (s/n): ').upper()

    if repetir == 'S':
        continue
    else:
        print('\nOBRIGADA POR JOGAR!!')
        break