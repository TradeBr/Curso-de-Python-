valores = []

for c in range(0,5):
    valor = int(input('Digite um valor: '))
    if c == 0:
        valores.append(valor)
        print('Valor adicionado com sucesso no final da lista')
    if  c == 1 and valor < max(valores):
        valores.insert(0, valor)
        print('Valor adicionado com sucesso no inicio da lista')
    elif c == 1 and valor > max(valores):
        valores.append(valor)
        print('Valor adicionado com sucesso no final da lista')
    if valor < min(valores):
        valores.insert(0, valor)
        print('Valor adicionado com sucesso no inicio da lista')
    if valor > max(valores):
        valores.append(valor)
        print('Valor adicionado com sucesso no final da lista')
    if c == 3:
        if valor > valores[1] and valor < valores[2]:
            valores.insert(-1, valor)
        elif valor > valores[0] and valor < valores[1]:
            valores.insert(-2, valor)
print(valores)




