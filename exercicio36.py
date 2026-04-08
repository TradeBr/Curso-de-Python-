casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Quantos anos de financiamento? '))
meses = anos * 12
vfinanciamento = casa / meses
if vfinanciamento > salario * 0.3:
    print('Seu financiamento foi negado!')
else:
    print('Seu financiamento foi aprovado!')



