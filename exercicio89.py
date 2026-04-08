estudantes = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    estudantes.append([nome, [nota1 ,nota2], media])
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar not in 'SsNn':
        print('Selecione uma opção adequada!')
        continuar = str(input('Quer continuar? [S/N] '))
    elif continuar in 'Nn':
        break

print('-'*60)
for c in range(0, len(estudantes)):
    print(f' {'N°:':<4}{c+1:<4} {'NOME: ':<10}{estudantes[c][0]:<9} {'MÉDIA: ':>8} {estudantes[c][2]:>1}                  ' )
print('-'*60)

while True:
    print('-'*60)
    opção = int(input('Quer mostrar a nota de qual aluno?(999 encerra) '))
    if opção in range(0, len(estudantes)+1):
        print(f'As notas do estudante {opção} é {estudantes[opção-1][1]}')
    elif opção not in range(0, len(estudantes)+1):
        print('Escolha uma opção válida.')
    elif opção == 999:
        break
    print('-' * 60)