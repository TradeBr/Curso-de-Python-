soma = 0

for c in range(1,501):
    if c % 3 == 0:
        print(c)
        soma = soma + c
print('A soma de todos os números multiplos de 3 de 1 a 500 é {}'.format(soma))
print('fim')