linha1 = float(input("Digite uma linha: "))
linha2 = float(input("Digite uma linha: "))
linha3 = float(input("Digite uma linha: "))

if linha1 + linha2 > linha3 and linha2 + linha3 > linha1 and linha3 + linha1 > linha2:
    print('\033[0:32mForma um Triangulo!\033[m')
else:
    print('\033[0:31mNão forma um Triangulo!\033[m')

