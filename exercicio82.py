numeros = []
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    if num % 2 == 1:
        impares.append(num)

    opção = str(input('Quer continuar? [S/N] '))
    while opção not in 'SsNn':
        print('Digite uma opção válida!')
        opção = str(input('Quer continuar? [S/N] '))
    if opção in 'Nn':
        break

print(f'Os números informados foram {numeros}')
print(f'Os pares foram: {pares}')
print(f'Os impares foram: {impares}')