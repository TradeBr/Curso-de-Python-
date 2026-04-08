nasc = int(input('Digite seu ano de nascimento: '))
idade = 2026 - nasc
if idade > 18:
    print('Ja passou do tempo de se alistar!')
elif idade < 18:
    print('Você ainda não precisa, mas em breve vai se alistar!')
else:
    print('Você deve se alistar este ano.')