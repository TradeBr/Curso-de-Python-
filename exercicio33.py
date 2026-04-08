n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
ordem = [n1, n2, n3]
ordem.sort()
print('O maior número é o {} e o menor número é o {}'.format(ordem[2], ordem[0]))

