import random

aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print("A ordem ficou {} é o primeiro, {} é o segundo, {} vai ser o terceiro e {} o último".format( lista[0], lista[1], lista[2], lista[3]))
