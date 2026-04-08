from math import factorial
n = int(input('Digite um número: '))
f = 1
c = n
for i in range(n+1, 1, -1):
    f = f * c
    c = c - 1
    print(c+1 , ' x ' if c > 0 else ' = ', end='')
print('Logo o resultado desse fatorial é igual a {}'.format(f))

"""
while n != -1:
    n = int(input('Digite um número(-1 Encerra): '))
    if n != -1:
        f = factorial(n)
        print('O valor do fatorial de {} é {}'.format(n, f))
print('Fim do programa') 
"""



