def terreno(a, b):
    area = a * b
    print('-'*30)
    print(f'A área do terreno de {a}m x {b}m totaliza {area:.2f}m²')


#PROGRAMA PRINCIPAL - Área de um terreno.
a = float(input('Qual a Largura do terreno em m? '))
b = float(input('Qual o Comprimento do terreno em m? '))
terreno(a, b)
