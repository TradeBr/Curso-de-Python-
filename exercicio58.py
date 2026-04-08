import random
# Jogo de Pedra Papel e Tesoura

'''
movimentos = ['PEDRA', 'PAPEL', 'TESOURA']
condição = ''
c = 0

while condição != 'VITÓRIA':
    movjogador = str(input('Pedra, Papel ou Tesoura? ')).upper()
    movcomputador = random.choice(movimentos)

    if movjogador != 'PEDRA' and movjogador != 'PAPEL' and movjogador != 'TESOURA':
        print('Escolha um movimento corretamente!')

    print()
    if movjogador =='PEDRA' and movcomputador == 'TESOURA':
        condição = 'VITÓRIA'
        print('Você venceu, seu movimento foi {} e do computador foi {}.'.format(movjogador, movcomputador))

    if movjogador =='PEDRA' and movcomputador == 'PAPEL':
        condição = 'DERROTA'
        print('Você perdeu, seu movimento foi {} e do computador foi {}.'.format(movjogador, movcomputador))

    if movjogador =='TESOURA' and movcomputador == 'PEDRA':
        condição = 'DERROTA'
        print('Você perdeu, seu movimento foi {} e do computador foi {}.'.format(movjogador, movcomputador))

    if movjogador =='TESOURA' and movcomputador == 'PAPEL':
        condição = 'VITÓRIA'
        print('Você venceu, seu movimento foi {} e do computador foi {}.'.format(movjogador, movcomputador))

    if movjogador == 'PAPEL' and movcomputador == 'TESOURA':
        condição = 'DERROTA'
        print('Você perdeu, seu movimento foi {} e do computador foi {}.'.format(movjogador, movcomputador))

    if movjogador =='PAPEL' and movcomputador == 'PEDRA':
        condição = 'VITÓRIA'
        print('Você venceu, seu movimento foi {} e do computador foi {}.'.format(movjogador, movcomputador))

    if movjogador == movcomputador:
        print('Os movimentos foram: {} e {}'.format(movjogador, movcomputador))
        print('Por conta dos movimentos serem iguais foi empate.')

    if condição == 'DERROTA':
        c += 1

print('VocÊ venceu e foi preciso {} movimentos.'.format(c)) '''

# Jogo da adivinhação do número
n = int(0)
i = 0
ncomputador = random.randint(0, 10)

while n != ncomputador:
    n = int(input('Digite um número: '))
    ncomputador = random.randint(0, 10)
    if n != ncomputador:
        print('Você errou! Tente novamente! Eu pensei em {}.'.format(ncomputador))
        i += 1
print("Você acertou, você pensou em {} e eu no número {}.".format(n, ncomputador))
print('Foram necessárias {} tentativas.'.format(i))


