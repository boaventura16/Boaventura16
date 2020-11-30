lista = list()
pares = list()
impares = list()
while True:
    print('='*30)
    n = int(input('Digite um número: '))
    r = input('Quer continuar? [S/N]: ').upper().strip()
    lista.append(n)
    if r not in 'SN':
        print('Opção invalida:')
        r = input('Quer continuar? [S/N]: ')
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    if r == 'N':
        break
print('-'*30)
print(f'A lista completa é: {lista}')
print(f'A lista de números pares é: {pares}')
print(f'A lista de números impares é: {impares}')
