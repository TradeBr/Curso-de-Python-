np = 0
ni = 0
no = []

for c in range(1,7):
    n = int(input('Informe um número: '))
    no.append(n)
    if n % 2 == 0:
        np = np + n
    else:
        ni = ni + n
print('os números foram: {}'.format(no))
print('A soma dos números pares da {}'.format(np))
print('A soma dos números impares da {}'.format(ni))

