palavras = ('TUPI', 'GUARANI', 'LITERATURA', 'ROLEX', 'FOSFATO', 'LAPSO', 'ROXO')
for c in palavras:
    print(f' \nna palavra {c.upper()} temos: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

