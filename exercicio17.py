import math

ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
h = math.pow(ca, 2) + math.pow(co, 2)
hr = math.pow(h, 1/2)
print("Então o valor da hipotenusa é igual a {}".format(hr))
