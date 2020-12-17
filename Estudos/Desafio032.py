dados = {}
lista = list()
gols = []
while True:
  dados.clear()
  dados['jogador'] = input('Nome: ')
  r = int(input(f'Quantos jogos {dados["jogador"]} fez: '))
  for c in range(1, r+1):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
  dados['gols'] = gols[:]
  dados['total'] = sum(dados['gols'])
  lista.append(dados.copy())
  gols.clear()
  while True:
    resposta = input('Quer continuar [S/N]: ').upper()
    if resposta in 'SN':
      break
    print('ERRO! Opção invalida, digite S ou N.')
  if resposta in 'N':
    break
print('-='*30)
print(f'Cod', end=' ')
for i in dados.keys():
  print(f'{i:<15}', end=' ')
print()
print('-'*40)
for k, v in enumerate(lista):
  print(f'{k:>3}', end=' ')
  for d in v.values():
    print(f'{str(d):<15}', end=' ')
  print()
print('-'*40)
while True:
  busca = int(input('Quer mostrar dados de qual jogador? [999] para parar. '))
  if busca == 999:
    break
  if busca > len(lista):
    print('ERRO! Esse jogador não existe.')
  else:
    print(f' --- LEVANTAMETO DE JOGADOR {lista[busca]["jogador"]}: ')
    for i, g in enumerate(lista[busca]['gols']):
      print(f'   No jogo {i+1} fez {g} gols')
  print('-'*40)
print('<< VOLTE SEMPRE >>')
