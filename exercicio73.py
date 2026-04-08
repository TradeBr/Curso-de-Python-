from random import choice

times = ('Palmeiras', 'Athlético-PR', 'São Paulo', 'Fluminense', 'Flamengo', 'Bahia', 'Coritiba', 'Grêmio', 'Vasco', 'Vitória', 'Corinthians', 'Internacional', 'Atlético-MG', 'RB Bragantino', 'Chapecoense', 'Santos', 'Botafogo', 'Mirassol', 'Remo', 'Cruzeiro')
c = 0
i = len(times) - 1
print('O top 5 é: \n')
print('-'*50)
for c in range(0, 5):
    print(f'{c+1}° é o time {times[c]}')
    c+=1
print('-'*50)

print('Os que estão na Zona de Rebaixamento são os times: \n')
print('-'*50)
for c in range(i,15, -1):
    print(f'{i+1}° é o time {times[i]}')
    i-=1

print('-'*50)
print('Segue lista ordenada por ordem Alfabética:')
for c in range(0, 20):
    print(sorted(times)[c])
print('-'*50)

print(f'O time da chapecoense está na posição: {times.index("Chapecoense")+1}')

