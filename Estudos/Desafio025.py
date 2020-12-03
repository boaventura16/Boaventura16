lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = scol = slin = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor para {[l], [c]}: '))
print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end=' ')
        if lista[l][c] % 2 == 0:
            spar += lista[l][c]
    print()
print('~~'*30)
print(f'A soma dos números pares são: {spar}')
for l in range(0, 3):
    scol += lista[l][2]
print('~~'*30)
print(f'A soma da coluna 3 é: {scol}')
for c in range(0, 3):
    slin += lista[2][c]
print('~~'*30)
print(f'A soma da linha 3 é: {slin}')
for c in range(0, 3):
    if c == 0:
        maior = lista[1][c]
    elif lista[1][c] > maior:
        maior = lista[1][c]
print('~~'*30)
print(f'O maior número da linha 2 é: {maior}')
