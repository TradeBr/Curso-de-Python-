from random import randint

jogo = int(input('Quantos jogos deseja jogar? '))
print('-'*30)
for c in range(0, jogo):
    dados = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    print(f'Jogo {c+1}: {dados[:]}', end=' ')
    dados.clear()
    print()
print('-'*30)