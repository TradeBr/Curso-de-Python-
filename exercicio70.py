soma = 0
acima = 0
menor = 0
pmenor = ''

while True:

    print('-' * 30)
    nproduto = str(input('Digite o nome do produto: ')).title().strip()
    produto = float(input('Digite o valor do produto: '))
    soma += produto
    print('-' * 30)
    opção = str(input('Quer continuar? [S/N]')).strip().upper()
    while opção not in 'SN':
        print('Digite uma opção válida!')
        opção = str(input('Quer continuar? [S/N]')).strip().upper()

    #guarda os produtos acima de R$1000
    if produto > 1000:
        acima += 1

    #determina o produto de menor valor
    if produto > menor and menor == 0:
        pmenor = nproduto
        menor = produto
    else:
        if produto < menor:
            pmenor = nproduto
            menor = produto

    if opção == 'N':
        break

print(f'A soma total foi de {soma:.2f}')
print(f'A quantidade de produtos acima de R$1000 foi de {acima}')
print(f'O produto de menor valor foi o {pmenor} no valor de {menor:.2f}')