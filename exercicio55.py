pesos = []
for c in range(1,6):
    peso = int(input('Digite o seu peso: '))
    pesos.append(peso)
pesos.sort()
maior = pesos[-1]
menor = pesos[0]
print('O maior peso é o {}'.format(maior))
print('O menor peso é o {}'.format(menor))

