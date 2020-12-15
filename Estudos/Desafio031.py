from datetime import datetime
dados = dict()
dados['nome'] = input('Nome: ')
data = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - data
dados['ctps'] = int(input('Número da carteira de trabalho. (0 não tem): '))
if dados['ctps'] == 0:
    pritn()
    print('========== Dados ==========')
    for v, k in dados.items():
        print(f' - {v} tem o valor {k}.')
    print()
if dados['ctps'] != 0:
    ano = int(input('Ano de contratação: '))
    dados['contratação'] = ano
    dados['salario: '] = float(input('Sálario: R$'))
    dados['aposentadoria'] = ano - data + 35
    print()
    print('========== Dados ==========')
    for v, k in dados.items():
        print(f' - {v} tem o valor {k}.')
print()
