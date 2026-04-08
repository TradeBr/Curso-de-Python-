pessoas = []
dados = []
pesadas = []
leves = []
acima = 0
abaixo = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    opção = str(input('Deseja adicionar mais uma pessoa? [S/N]'))
    if opção not in 'SsNn':
        print('Escolha uma opção válida!')
        opção = str(input('Deseja adicionar mais uma pessoa? [S/N]'))
    elif opção in 'Nn':
        break

for c in range(0,len(pessoas)):
    if pessoas[c][1] > 100:
        pesadas.append(pessoas[c][:])
        acima +=1
    elif pessoas[c][1] < 100:
        leves.append(pessoas[c][:])
        abaixo +=1

print(f'A quantidade de pessoas foi de {len(pessoas)} pessoas')
print(f'A quantidade de pessoas acima de 100kg foi de {acima} pessoas')
print(f'As pessoas que estão acima são {pesadas}.')
print(f'A quantidade de pessoas abaixo de 100kg foi de {abaixo} pessoas')
print(f'As pessoas que estão abaixo são: {leves}')