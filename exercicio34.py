salario = float(input('Digite o valor do seu salário: '))
if salario > 1250:
    aumento = salario * 0.10
    novosalario = salario + aumento
    print('Com o aumento, seu novo salário ficou com o valor de {}.'.format(novosalario))
else:
    aumento = salario * 0.15
    novosalario = salario + aumento
    print('Com o aumento, seu novo salário ficou com o valor de {}.'.format(novosalario))