op = 0
n1 = 0
n2 = 0
res = 0
maior = 0
menor = 0

while op != 5:
    n1 = float(input('Primeiro número: '))
    n2 = float (input('Segundo número:'))
    print('-'*30)
    print(""" 
    [1] Somar
    [2] Multiplicar  
    [3] Maior 
    [4] Digitar novos números
    [5] Sair do programa
    """)
    print('-' * 30)
    op = int(input('Deseja realizar qual operação?'))
    if op == 1:
        res= n1 + n2
        print('A resposta dessa Soma é {}.'.format(res))
    elif op == 2:
        res = n1 * n2
        print('A resposta dessa multiplicação é {}'.format(res))
    elif op == 3:
        if n1 > n2:
            maior = n1
            menor = n2
            print('O maior número foi {} e o menor {}.'.format(maior, menor))
        else:
            maior = n2
            menor = n1
            print('O maior número foi {} e o menor {}.'.format(maior, menor))
    elif op == 4:
        continue
    elif op == 5:
        print('Finalizando...')
    else:
        print('Selecione uma opção válida.')
print('FIM DO PROGRAMA')



