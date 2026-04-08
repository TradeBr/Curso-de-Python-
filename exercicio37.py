num = int(input('Informe um número: '))
print('Deseja fazer qual tipo de transformação?')
print('1 - Binario\n' 
      '2 - Octal\n'
      '3 - Hexadecimal\n')

res = input()
if res == '1':
    binario = bin(num)[2:]
    print(binario)
elif  res == '2':
    octal = oct(num)[2:]
    print(octal)
elif res == '3':
    hexadecimal = hex(num)[2:]
    print(hexadecimal)
else:
    print("Selecione uma das opções!")