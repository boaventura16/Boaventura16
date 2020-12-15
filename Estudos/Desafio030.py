from random import randint
from time import sleep
from operator import itemgetter
dado = {'jogador 1': randint(1, 6),
'jogador 2': randint(1, 6),
'jogador 3': randint(1, 6),
'jogador 4': randint(1, 6)}
ranking = list()
print('====== JOGANDO OS DADOS ======')
for v, k in dado.items():
    print(f'O {v} jogou o número {k}')
    sleep(1)
print()
print('-'*30)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print('~~~~ RANKING DIS JOGADORES ~~~~')
for i, c in enumerate(ranking):
    print(f'{i + 1}º Lugar: {c[0]} com {c[1]}')
print()
print(FIM)
