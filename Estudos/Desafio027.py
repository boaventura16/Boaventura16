lista = []
temp = []
media = s = cont = 0
while True:
    temp.append(input('Nome do aluno: '))
    temp.append(float(input('Primeira nota do aluno: ')))
    temp.append(float(input('Segunda nota do aluno: ')))
    r = input('Continuar a cadastrar? [S/N]: ').upper().strip()
    s = temp[1] + temp[2]
    media = s / 2 
    temp.append(media)
    lista.append(temp[:])
    temp.clear()
    if r == 'N':
        break
print('='*30)
print(f'{"Nº":<4}{"Aluno":<10}{"Média":>8}')
print('-'*30)
for i, c in enumerate(lista):
    print(f'{i:<4}{c[0]:<10}{c[3]:>8.1f}')
print('-'*30)
while True:
    resp = int(input('Mostrar notas de qual aluno: (999 para encerrar.)'))
    if resp == 999:
        break
    if resp <= len(lista) - 1:
        print('~'*30)
        print(f'As notas do aluno(a) {lista[resp][0]} foram: {lista[resp][1]} e {lista[resp][2]}')
        print('~'*30)
print('Volte sempre!')
