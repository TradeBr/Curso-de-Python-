maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento: '))
    idade = 2025 - ano
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('A quantidade de pessoas maior de idade são: {}'.format(maior))
print('A quantidade de pessoas menores de idade são: {}'.format(menor))

