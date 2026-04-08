cidade = str(input('Digite o nome de uma cidade: ')).strip()
cidades = cidade.split()
cmcs = cidades[0].upper()
cmc = 'SANTO' in cmcs
print(cidades[0])
print('A cidade começa com Santo? {}'.format(cmc))


