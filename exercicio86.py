tabela = []
dados = []

for l in range(1,4):
    for c in range(1,4):
        dados.append(int(input(f'Digite um número para a linha {l} da coluna {c}:')))
    tabela.append(dados[:])
    dados.clear()

for i in range(0,len(tabela)):

    print(f'{str(tabela[i]):^5}', end=' ')
    print()

