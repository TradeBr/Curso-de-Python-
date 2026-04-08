import random

v = 0
d = 0
njogador = 0
ncomputador = 0
resultado = 0

while True:
    jogo = str(input('Impar ou Par?')).strip().upper()

    if jogo == 'PAR':
        print('Você é par, o computador vai ser o número impar.')
        njogador = int(input('Digite o seu número(De 1 a 10): '))
        if njogador not in range(1, 10):
            print('Selecione um movimento válido')
            njogador = int(input('Digite o seu número(De 1 a 10): '))

    elif jogo == 'IMPAR':
        print('Você é impar, o computador vai ser o número par.')
        njogador = int(input('Digite o seu número(De 1 a 10): '))
        if njogador not in range(1, 10):
            print('Selecione um movimento válido')
            njogador = int(input('Digite o seu número(De 1 a 10): '))

    elif jogo != 'PAR' and jogo != 'IMPAR':
        print('Selecione uma opção valida')
        jogo = str(input('Impar ou Par?')).strip().upper()

    ncomputador = random.randint(1, 10)

    resultado = njogador + ncomputador

    if resultado % 2 == 0 and jogo == 'PAR':
        print(f'O jogador escolheu o número {njogador} e o computador escolheu {ncomputador} o resultado foi {resultado} e com isso: ')
        print('JOGADOR VENCEU!')
        v+=1
    elif resultado % 2 == 1 and jogo == 'PAR':
        print(
        f'O jogador escolheu o número {njogador} e o computador escolheu {ncomputador} o resultado foi {resultado} e com isso: ')
        print('JOGADOR PERDEU!')
        d +=1

    if resultado % 2 == 1 and jogo == 'IMPAR':
        print(
        f'O jogador escolheu o número {njogador} e o computador escolheu {ncomputador} o resultado foi {resultado} e com isso: ')
        print('JOGADOR VENCEU!')
        v += 1
    elif resultado % 2 == 0 and jogo == 'IMPAR':
        print(
        f'O jogador escolheu o número {njogador} e o computador escolheu {ncomputador} o resultado foi {resultado} e com isso: ')
        print('JOGADOR PERDEU!')
        d+=1

    if d > 0:
        break

    if v > 1:
        print(f'Infelizmente o Jogador perdeu, mas teve uma sequencia de {v} Vitórias.')
    else:
        print(f'Infelizmente o Jogador perdeu, e teve apenas uma Vitória.')


