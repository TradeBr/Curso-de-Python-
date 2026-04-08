continuar = ''
n = 0
soma = 0
maior = 0
menor = 0
c = 0
while continuar != 'N':
    n = int(input('Digite um número: '))
    c+=1
    soma += n
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    while continuar not in 'SsNn':
        print('Digite uma resposta válida.')
        continuar = str(input('Quer continuar? [S/N] ')).upper()
    if n > 0 and maior == 0:
        maior = n
    if n > maior:
        maior = n
    if n < maior:
        menor = n
if menor == 0:
    print('Você informou apenas um número: {}'.format(maior))
else:
    print(f'O maior número informado foi {maior} e o menor foi {menor}')
media = soma / c
print('A média entre os valores é {}'.format(media))
print('A soma de todos os números informados é {}'.format(soma))
print('Fim do programa')

