viagem = int(input('Qual a distancia da viagem? '))
if viagem <= 200:
    valor = viagem * 0.50
    print('O valor dessa viagem vai ser de R${}'.format(valor))
else:
    valor = viagem * 0.40
    print('O valor da viagem ser de R${}'.format(valor))
