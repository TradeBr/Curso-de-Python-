nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota1 = 0

while True:
    saque = int(input('Informe o valor que deseja sacar: R$ '))
    while saque != 0:
        if saque - 50 > 0:
            nota50 = saque // 50
            saque = saque - (nota50 * 50)
        elif saque - 20 > 0:
            nota20 = saque // 20
            saque = saque - (nota20 * 20)
        elif saque - 10 > 0:
            nota10 = saque // 10
            saque = saque - (nota10 * 10)
        elif saque - 5 > 0:
            nota5 = saque // 5
            saque = saque - (nota5 * 5)
        elif saque - 1 > 0:
            nota1 = saque // 1
            saque = saque - (nota1 * 1)
    if saque == 0:
        break
print(f'A quantidade de notas foram: {nota50} notas de 50, {nota20} notas de vinte, {nota10} notas de 10, {nota5} notas de 5 e {nota1} notas de 1')