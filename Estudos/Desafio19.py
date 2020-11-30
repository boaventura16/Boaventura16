c = 0
lista = list()
while True:
    print('='*30)
    n = int(input('Digite um número: '))
    lista.append(n)
    r = input('Quer Continuar? [S/N]: ').upper().strip()
    c += 1
    if r not in 'SN':
        print('Opção invalida.')
        r = input('Quer continuar? [S/N]: ')
    if r == 'N':
        if 5 in lista:
            print('='*30)
            print(f'O número 5 está na lista.')
        else:
            print('='*30)
            print('O número 5 não está na lista;')
        break
print(f'Você digitou {c} números.')
print(f'Os números em ordem decrescente são: {sorted(lista, reverse=True)}')
