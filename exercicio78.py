valores = []

for c in range(0,5):
    num = int(input('Digite um valor: '))
    valores.append(num)

valores.sort()

print(f'Os valores informados foram {valores}')
print(f'O maior valor informado foi {max(valores)} e sua posição na lista é {valores.index(max(valores))+1}')
print(f'O menor valor informado foi {min(valores)} e sua posição na lista é {valores.index(min(valores))+1}')