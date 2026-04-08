ninicial = int(input('Número de inicio: '))
razao = int(input('Digite a Razão: '))
q = int(input('Quantos termos deseja mostrar(Para encerrar digite 0): '))
c = 0
if q == 0:
    print('Fim do programa')
else:
    while c < q:
        print(ninicial)
        ninicial += razao
        c += 1
print('Fim do programa')

