# Forma que eu fiz
#num = input('Digite um número de 1 a 9999: ')
#len(num)
#if len(num)==1:
#    print('Seu número é o {}'.format(num))
#if len(num)==2:
#    print('Seu número é o {}'.format(num))
#    print('Seu número tem {} Dezenas.'.format(num[0]))
#    print('Seu número tem {} Unidades.'.format(num[1]))
#if len(num)==3:
#    print('Seu número é o {}'.format(num))
#    print('Seu número tem {} Centenas.'.format(num[0]))
#    print('Seu número tem {} Dezenas.'.format(num[1]))
#    print('Seu número tem {} Unidades.'.format(num[2]))
#if len(num)==4:
#   print('Seu número é o {}'.format(num))
#    print('Seu número tem {} Milhares.'.format(num[0]))
#    print('Seu número tem {} Centenas.'.format(num[1]))
#    print('Seu número tem {} Dezenas.'.format(num[2]))
#    print('Seu número tem {} Unidades.'.format(num[3]))
#Jeito da Aula:
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('A unidade é {}'.format(u))
print('O decimal é {}'.format(d))
print('A centena é {}'.format(c))
print('E o milhar é {}'.format(m))

