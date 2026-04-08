n9 = 0
pares = 0
p3 = 0

numeros = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')))
print(numeros)

for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        pares += 1

print(f'A quantidade de pares é: {pares}')
if 9 in numeros:
    n9 += 1
    print(f'A quantidade de 9 é {n9}')
else:
    print('Não foi informado nenhum número 9.')

if 3 in numeros:
    print(f'A primeira posição do 3 é {numeros.index(3)+1}')
else:
    print('Não foi informado o número 3.')

