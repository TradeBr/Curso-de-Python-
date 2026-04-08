radar = int(input('Qual a velocidade do carro que foi detectada? '))
if radar > 80:
    print('Você foi multado!')
    valorm = float((radar - 80) * 7.0)
    print('O valor da multa é de R${}'.format(valorm))
else:
    print('Ele está dentro da velocidade permitida na via.')
