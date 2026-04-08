import math

n = int(input('digite um numero inteiro: '))
if n > 1:
    for c in range(2, int(math.sqrt(n)), 1):
        if n % c == 0:
            print('O número não é primo')
        else:
            print('O número é primo')
else:
    print('O número primo não pode ser 0 e nem 1.')
print('FIM')
