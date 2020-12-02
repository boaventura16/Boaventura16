lista = [[], []]
temp = 0
par = impar = c = 0
for n in range(1, 8):
    temp = int(input(f'Digite o {n}º número: '))
    if temp % 2 == 0:
        lista[0].append(temp)
    if temp % 2 == 1:
        lista[1].append(temp)
print('=-'*30)
print(f'Os valores \033[1;34mPARES\033[m digitados foram: {sorted(lista[0])}')
print(f'Os valores \033[1;35mIMPARES\033[m digitados foram: {sorted(lista[1])}')
