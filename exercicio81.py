valores = []
c =0

while True:
    valor = int(input('Digite um valor: '))
    c+=1
    valores.append(valor)

    opção = str(input('Deseja continuar? [S/N] '))
    while opção not in 'SsNn':
        print('Digite uma opção válida!')
        opção = str(input('Deseja continuar? [S/N] '))
    if opção in 'Nn':
        break

print(f'A quantidade de números informados foi {c}')
valores.sort(reverse=True)
print(valores)
if 5 in valores:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista.')

