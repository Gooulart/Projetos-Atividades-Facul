divida_total = int(input("Insira o valor de sua Dívida TOTAL: "))
mensalidade = int(input("Insira o valor da mensalidade: "))
i = 0
restante = 0

while divida_total > 0:
    if mensalidade < divida_total:
        i += 1
        divida_atual = divida_total
        restante = divida_total - mensalidade
        print(f'Valor da Mensalidade: {mensalidade}')
        print(f'pagamento: {i}')
        print(f'Valor atual = {divida_total}')
        divida_total -= mensalidade
        print(f'Restante = {restante}')
        print('-----')
    else:
        i +=1
        print(f'Valor da Mensalidade: {mensalidade}')
        print(f'pagamento: {i}')
        print(f'Valor atual = {divida_total}')
        print(f'Restante = 0')
        print('-----')
        break
