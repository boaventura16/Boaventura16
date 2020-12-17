def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos valores {valores} é = {s}')


soma(2, 3, 4)
soma(1, 5)
