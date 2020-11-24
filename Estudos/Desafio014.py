print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)
n = int(input('Digite a quantidade de sequências: '))
print('~')
t1 = 0
t2 = 1
c = 0
print('{} → {}'.format(t1, t2), end = '')
while c <= n:
    t3 = t1 + t2
    c += 1
    t1 = t2
    t2 = t3
    print(' → {}'.format(t3), end = '')
print('→ FIM')
