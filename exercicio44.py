produto = float(input('Digite o valor do produto: '))
print('1- A vista no dinheiro/cheque \n 2- Á vista no cartão \n 3- Em até 2 vezes no cartão \n 4- 3x ou mais no cartão')
pagamento = float(input('qual vai ser o método de pagamento? '))
if pagamento == 1:
    desconto = produto * 0.10
    pd = produto - desconto
    print('Vai ter 10% de desconto!')
    print('O produto que era R${} com o desconto no valor de R${}, será pago o valor de R${}.'.format(produto, desconto, pd))
if pagamento == 2:
    desconto = produto * 0.05
    pd = produto - desconto
    print('Vai ter 5% de desconto!')
    print('O produto que era R${} com o desconto no valor de R${}, será pago o valor de R${}.'.format(produto, desconto, pd))
if pagamento == 3:
    print('Será pago o valor normal do produto que é de {}'.format(produto))
if pagamento == 4:
    juros = produto * 0.20
    pj = produto + juros
    print('Vai ter 20% de juros ')
    print('O produto que era R${} vai ser aplicado o juros de R${}, será pago o valor de R${}.'.format(produto, juros, pj))