linha1 = float(input('Digite a primeira linha: '))
linha2 = float(input('Digite a segunda linha: '))
linha3 = float(input('Digite a terceira linha: '))
if linha1 + linha2 > linha3 and linha1 + linha3 > linha2 and linha3 + linha1 > linha2 and linha3 + linha2 > linha1:
    triangulo = str('Forma um Triangulo!')
else:
    triangulo = str('Não forma um Triangulo!')

res = triangulo.upper()
print(res)
if res == 'NÃO FORMA UM TRIANGULO!':
    print("Não formou um triangulo, tente novamente.")
else:
    if linha1 == linha2 and linha2 == linha3 and linha3 == linha1:
        print('Forma um Triangulo e ele é um triangulo Equilátero ja que tem todos os lados iguais.')
    elif linha1 == linha2  or linha2 == linha3 or linha3 == linha1:
        print('Forma um Triangulo e ele é um triangulo Isósceles, ja que tem dois lados iguais.')
    elif linha1 != linha2 and linha2 != linha3 and linha3 != linha1:
        print('Forma um triangulo Escaleno, em que todos os lados são diferentes.')