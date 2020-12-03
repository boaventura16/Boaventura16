from random import randint
from time import sleep
lista = []
temp = []
total = 1
print('-'*30)
print('      JOGUE NA MEGA      ')
print('-'*30)
p = int(input('Quantos jogos deseja fazer? '))
while total <= p:
    cont = 0
    while True:
        num = randint(1, 60)
        cont += 1
        if num not in temp:
            temp.append(num)
        if cont >= 6:
            break
    temp.sort()
    lista.append(temp[:])
    temp.clear()
    total += 1
print('-'*30)
print()
print('='*3, f'ESCOLHENDO {total} JOGOS ALEATORIOS', '='*3)
print()
for i, l in enumerate(lista):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print()
print('~~'*5, '< BOA SORTE! >', '~~'*5)
