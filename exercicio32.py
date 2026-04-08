from datetime import date
anob = int(input('Informe um ano: (Digite 0 para pegar o ano atual)'))
if anob == 0:
    anob = date.today().year
if anob % 4 == 0 and anob % 100 != 0 or anob % 400 == 0:
    print('O ano é Bissexto!')
else:
    print('O ano não é Bissexto!')