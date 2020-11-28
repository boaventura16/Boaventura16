num = []
maior = menor = 0
for n in range(0, 5):
    num.append(int(input(f'Digite o número na posição {n}: ')))
    if n == 0:
        maior = menor = num[n]
    else:
        if num[n] > maior:
            maior = num[n]
        if num[n] < menor:
            menor = num[n]
print(f'Os números digitados foram: {num}')
print(f'O maior número é o {maior} e ele aparece nas posições:', end=' ')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end=' ')
print()
print(f'O menor número é o {menor} e ele aparece nas posições:', end=' ')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end=' ')
print()
