import random

'''Jogador'''
print('Você jogador deseja jogar qual movimento?')
print('Tesoura \n Pedra \n Papel')
movimento = str(input('Qual o movimento? ').upper())
'''Computador'''
movimentos = ['Pedra', 'Papel', 'Tesoura']
selecionado = str(random.choice(movimentos).upper())
if movimento == selecionado:
    print('empatou, ambos selecionaram os mesmos. {} e {}'.format(movimento, selecionado))
if movimento == 'PEDRA' and selecionado == 'PAPEL':
    print('Os movimentos foram {} e {} então:'.format(movimento, selecionado))
    print('o Computador ganhou!')
if movimento == 'PEDRA' and selecionado == 'TESOURA':
    print('Os movimentos foram {} e {} então:'.format(movimento, selecionado))
    print('o Jogador ganhou!')
if movimento == 'PAPEL' and selecionado == 'TESOURA':
    print('Os movimentos foram {} e {} então:'.format(movimento, selecionado))
    print('o Computador ganhou!')
if movimento == 'PAPEL' and selecionado == 'PEDRA':
    print('Os movimentos foram {} e {} então:'.format(movimento, selecionado))
    print('o Jogador ganhou!')
if movimento == 'TESOURA' and selecionado == 'PEDRA':
    print('Os movimentos foram {} e {} então:'.format(movimento, selecionado))
    print('o Computador ganhou!')
if movimento == 'TESOURA' and selecionado == 'PAPEL':
    print('Os movimentos foram {} e {} então:'.format(movimento, selecionado))
    print('O Jogador ganhou!')
else:
    print('Por conta dos movimentos {} e {}, ninguém perdeu.'.format(movimento, selecionado))


