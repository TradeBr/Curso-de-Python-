while True:
    n = int(input('Digite o número que deseja a tabuada: '))
    if n > 0:
        for c in range (1, 11):
            print(f'{n} x {c} = {n * c}')
    else:
        break
print('FIM DO PROGRAMA')