boletim = dict()
boletim['nome'] = input('Nome do Aluno: ')
boletim['media'] = float(input(f'Media do Aluno {boletim["nome"]}: '))
print('~'*30)
print(f'O nome é igual á {boletim["nome"]}')
print(f'A media é igual a {boletim["media"]}')
if boletim['media'] < 7:
    print(f'O aluno(a) {boletim["nome"]} está reprovado.')
else:
    print(f'O aluno(a) {boletim["nome"]} está aprovado')
