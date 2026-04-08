sexo = ' '
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    if sexo == 'M' or sexo == 'F':
        print('Sexo {} válido !'.format(sexo))
    else:
        print('Sexo {} inválido !'.format(sexo))



