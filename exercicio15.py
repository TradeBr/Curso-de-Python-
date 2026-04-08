dias = int(input('O carro rodou por quantos dias? '))
kms = float(input('Quantos km foram percorridos? '))
vd = dias *60
vkm = kms * 0.15
vt = vd + vkm
print('O valor a ser pago por, {} dias e {} kilometros é de {:.2f}R$'.format(dias, kms, vt))