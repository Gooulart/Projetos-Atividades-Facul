def ordenacao_em_bolha(sequencia):
    tamanho = len(sequencia)
    for i in range(tamanho):
        for j in range(0, tamanho - i - 1):
            if sequencia[j] > sequencia[j + 1]:
                sequencia[j], sequencia[j + 1] = sequencia[j + 1], sequencia[j]

lista = [4, 1, 3, 2, 10, 5, 9, 8, 7, 6]

ordenacao_em_bolha(lista)
print(lista)
