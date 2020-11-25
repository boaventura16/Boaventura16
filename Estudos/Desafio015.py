print('='*30)
print('{:^30}'.format('Banco ML'))
print('='*30)
valor = int(input('Valor a ser sacado: R$'))
totced = 0
ced = 50
while True:
    if valor >= ced:
        valor -= 50
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de {ced} foram sacadas.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if valor == 0:
            break
print('Operação Finalizada.')
