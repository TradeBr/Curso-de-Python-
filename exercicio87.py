tabela = []
dados = []
soma = 0
terceiracoluna = 0
maiorsegunda = 0
for l in range(1,4):
    for c in range(1,4):
        valor = int(input(f'Digite um número para a linha {l} da coluna {c}:'))
        dados.append(valor)
        if valor % 2 == 0:
            soma += valor
        if c == 3:
            terceiracoluna += valor
        if l == 2 and maiorsegunda == 0:
            maiorsegunda = valor
        elif l == 2 and maiorsegunda < valor:
            maiorsegunda = valor
    tabela.append(dados[:])
    dados.clear()

for i in range(0,len(tabela)):

    print(f'{str(tabela[i]):^5}', end=' ')
    print()

print(f'A soma de todos os pares é igual á {soma}')
print(f'A soma dos elementos da terceira coluna é igual á {terceiracoluna}')
print(f'O maior elemento da segunda linha é o: {maiorsegunda}')

