salario = float(input("Qual o valor do seu salário? "))
reajuste = salario*0.15
novo = salario+reajuste
print('Com o reajuste de 15% seu novo salário vai ser de \033[0:32mR${}\033[m'.format(novo))
