lista = list()
dados = list()
total = maior = menor = 0
while True:
    dados.append(input('Nome da pessoa: '))
    dados.append(int(input('Peso da pessoa: ')))
    r = input('Quer continuar? [S/N]: ').upper().strip()
    total += 1 
    if r not in 'NS':
        print('Opção invalida:')
        r = input('Quer continuar? [S/N]: ').upper().strip()
    if len(lista) == 0:
        maior = menor = dados[1]
    else: 
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    if r == 'N':
        break
print('=-'*30)
print(f'O total de pessoas foram: {total}')
print(f'O maior peso é {maior}Kg. Peso de', end=' ')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end = ' ')
print()
print(f'O menor peso é {menor}Kg. Peso de', end=' ')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print()
