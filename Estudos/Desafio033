dados = dict()
lista = list()
s = media = 0
while True:
  dados.clear()
  dados['nome'] = input('Nome: ')
  while True:
    dados['sexo'] = input(f'Sexo de {dados["nome"]} [M/F]: ').upper()
    if dados['sexo'] in 'MF':
      break
    print('ERRO! Opção invalida, digite M ou F.')
  dados['idade'] = int(input(f'Idade de {dados["nome"]}: ')
  lista.append(dados.copy())
  s += dados['idade']
  media = s / len(lista)
  while True:
    r = input('Quer continuar? [S/N]: ').upper()
    if r in 'SN':
      break
    print('ERRO! Opção invalida, digite S ou N.')
  if r == 'N':
    break
print('-=' *30)
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'A media de Idade das pessoas cadastradas é de {media} anos')
print(f'As mulheres cadastradas foram: ', end='')
for p in lista:
  if p['sexo'] in 'F':
    print(f'{p['nome']}', end='')
  print()
print(f'As pessoas acima da média de idade são: ', end='')
for p in lista:
  if p['idade'] > media:
    print('   ')
    for v, k in p.items():
      print(f'{v} = {k}', end='')
    print()
print('<< Encerrado >>')
