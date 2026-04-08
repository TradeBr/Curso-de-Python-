q1 = 0
q2 = 0

operação = str(input('Digite uma expressão: '))

q1 = operação.count('(')
q2 = operação.count(')')

print(q1)
print(q2)

if q1 == q2:
    print("Operação válida!")
else:
    print('A operação teve um erro de digitação.')
