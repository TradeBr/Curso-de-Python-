import random

naleatorio = random.randint(0, 5)
print('Qual é o número que foi sorteado? (De 0 a 5)')
chute = int(input('Digite o seu chute: '))
if chute == naleatorio:
    print('Você acertou!')
else:
    print('Você errou!')
