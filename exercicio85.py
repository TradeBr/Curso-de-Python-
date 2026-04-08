numeros = [[], []]

while True:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    if num % 2 == 1:
        numeros[1].append(num)

    opção = str(input('Quer continuar? [S/N] ')).strip()
    if opção not in 'SsNn':
        print('Escolha uma opção correta!')
        opção = str(input('Quer continuar? [S/N] ')).strip()
    if opção in 'Nn':
        break
numeros[0].sort()
numeros[1].sort()
print(f'Você digitou  {len(numeros[0]) + len(numeros[1])} números')
print(f'Os pares são: {numeros[0]}')
print(f'Os impares são: {numeros[1]}')