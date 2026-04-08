nasc = int(input("Qual o ano de nascimento? "))
idade = 2026 - nasc
if idade <= 9:
    print('Você é um nadador MIRIM')
elif idade <= 14:
    print('Você é um nadador INFANTIL')
elif idade <= 19:
    print('Você é um nadador JUNIOR')
elif idade <= 20:
    print('Você é um nadador SENIOR')
else:
    print('Você é um nadador MASTER')
