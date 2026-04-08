import random

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

'''escolhido = random.randint(1,4)
if escolhido == 1:
    print('O aluno escolhido foi {}'.format(aluno1))
if escolhido == 2:
    print('O aluno escolhido foi {}'.format(aluno2))
if escolhido == 3:
    print('O aluno escolhido foi {}'.format(aluno3))
if escolhido == 4:
    print('O aluno escolhido foi {}'.format(aluno4)) '''

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print("O aluno escolhido foi {}".format(escolhido))
