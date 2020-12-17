from time import sleep
def contador(i, f, p):
    print('-='*20)
    print(f'Contando de {i} a {f} de {p} em {p}')
    sleep(1.5)

    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    if i <= f:
        c = i
        while c <= f:
            print(f'{c}', end=' ', flush = True)
            sleep(0.5)
            c += p
        print('FIM!')
    else:
        c = i
        while c >= f:
            print(f'{c}', end=' ', flush = True)
            sleep(0.5)
            c -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('='*30)
print('Agora é sua vez de escolher a contagem.')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)
