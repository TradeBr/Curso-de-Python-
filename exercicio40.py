nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1 + nota2) / 2
if m >= 7:
    print("Você foi APROVADO!")
elif m >= 5 and m <= 6.9:
    print("Você está de Recuperação.")
else:
    print("Você foi REPROVADO!")
