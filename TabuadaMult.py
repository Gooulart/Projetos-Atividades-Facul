a = int(input())
b = int(input())
i = 1
if b >= a:
    while a <= b:
        while i <= 10:
            print(f'{a} x {i} = {a*i}')
            i += 1
        print('-' * 10)
        i = 1
        a += 1
else:
    print("Nenhuma tabela no intervalo")

