nome = str(input("Qual o seu nome completo? "))
nomes = nome.split()
print(len(''.join(nomes)))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nomes[0],len(nomes[0])))
print(nome.upper())
print(nome.lower())

