nome = input()
fixo = float(input())
vendas = float(input())

comissao = vendas * 0.15
total = fixo + comissao

print(f'TOTAL = R$ {total:.2f}')
