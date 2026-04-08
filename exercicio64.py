num = 0
q = 0
soma = 0
while num != 999:
    num = int(input('Digite um número(999 encerra o programa): '))
    if num != 999:
        soma +=num
        q += 1
print('A quantidade de números foi {}.'.format(q))
print('A soma de todos os números válidos foram {}.'.format(soma))
print('Fim do programa')
