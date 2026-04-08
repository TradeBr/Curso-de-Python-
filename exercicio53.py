frase = str(input('Digite uma frase ou palavra: '))
fraser = frase.strip().upper()
fraseinverso = fraser[::-1]
if fraser == fraseinverso:
    print('Esse texto é um Palíndromo')
else:
    print('Esse texto não é um Palíndromo')

