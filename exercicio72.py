numeros = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20(999 encerra): '))
    if numero == 999:
        break
    elif numero not in range(0, 21):
        while (numero not in range(0, 21)):
            print('Digite um número válido.')
            numero = int(input('Digite um número entre 0 e 20: '))
    elif numero >= 0 and numero <= 20:
        print(f'o número {numero} se escreve: {numeros[numero]}')
        opção = str(input('Deseja continuar? [S/N]'))
        if opção in 'Nn':
            break
        elif opção in 'Ss':
            continue
        else:
            while (opção not in 'Nn' or 'Ss'):
                print('Escolha uma opção válida.')
                opção = str(input('Deseja continuar? [S/N]'))



