idades = []
maior = 0
menor = 0

for c in range(1, 6):
    nome = str(input('Digite o nome da pessoa: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [M/F]')).upper()
    idades.append(idade)

    if sexo == 'M':
        if idade > maior:
            maior = idade

    if sexo == 'F' and idade < 20:
        menor = menor + 1

midade = sum(idades) / len(idades)
print('A média das idades desse grupo de 5 pessoa é: {}'.format(midade))
print('A idade do homem mais velho é: {}'.format(maior))
print('A quantidade de mulheres menores de 20 anos é {}'.format(menor))







