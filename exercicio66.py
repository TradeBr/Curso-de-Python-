c = 0
soma = 0
while True:
    n = int(input('Digite um número(999 interrompe): '))

    if n == 999:
        break
    else:
        c += 1
        soma += n
print(f'Foi digitado {c} e a soma deles é {soma}')
