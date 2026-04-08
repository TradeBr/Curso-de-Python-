itens = ('Livro', 50, 'Caderno', 30, 'Caneta', 3, 'Lapis', 2, 'Notebook', 5000)
for c in range(0, len(itens)):
    if c % 2 == 0:
        print(f'{itens[c]:.<30}', end=' ')
    elif c % 2 == 1:
        print(f'R${itens[c]:>5.2f}')
