lista = []
while True:
    v = (int(input('Digite um número: ')))
    if v not in lista:
        print('Valor acrescentado a lista')
        lista.append(v)
    else:
        print('Esse valor já foi acrescentado e não podera ser acrescentado novamente.')
    cont = input('Deseja continuar? [S/N]: ').upper().strip()
    if cont not in 'SN':
        print('Opção invalida. escolha [S/N]')
        cont = input('Deseja continuar? [S/N]: ').upper().strip()
    if cont == 'N':
        break
print('='*30)
print(f'Os números escolhidos foram: {sorted(lista)}')
