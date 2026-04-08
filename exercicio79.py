valores = []

while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        while valor in valores:
            print('Numeros iguais não podem ser adicionados a lista')
            valor = int(input('Digite um valor: '))
    else:
        valores.append(valor)

    opção = str(input('Deseja continuar? [S/N]'))
    while opção not in 'SsNn' :
        print('Digite uma opção válida')
        opção = str(input('Deseja continuar? [S/N]'))
    if opção in 'Nn':
        break

valores.sort()
print(f'Os valores unicos informados foram: {valores}')