peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('Seu imc é {:.2f} e você:'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
if imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal')
if imc >= 25 and imc <= 30:
    print('Você está acima do peso')
if imc >= 30 and imc <= 40:
    print('Você está obeso')
if imc > 40:
    print('Você está com obesidade morbida')
