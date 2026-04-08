#Iniciando as variáveis
homens = 0
mulheres = 0
pessoas = 0

while True:

    #Pegando os Dados
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    opcao = str(input('Quer continuar? [S/N]')).strip().upper()

    # Adicionando os Dados
    if idade > 18:
        pessoas += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1

    #Exceções
    while sexo != 'M' and sexo != 'F':
        print('Selecione um sexo válido!')
        sexo = str(input('Sexo [M/F]: ')).strip().upper()

    while opcao != 'N' and opcao != 'S':
        print('Escolha uma opção válida!')
        opcao = str(input('Quer continuar? [S/N]')).strip().upper()

    # Parando o Programa
    if opcao == 'N':
        break

print(f'A quantidade de Pessoas acima de 18 anos é de {pessoas}')
print(f'A quantidade de Homens é de {homens}')
print(f'A quantidade de Mulheres abaixo de 20 anos é de {mulheres}')