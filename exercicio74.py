from random import randint

numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

maior = sorted(numeros)[0]
menor = sorted(numeros)[-1]
print(f'Os números gerados foram: {numeros[0:]}')

print(f'O maior número gerado foi {maior}')
print(f'O menor número gerado foi {menor}')