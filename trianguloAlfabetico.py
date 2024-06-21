quantas_linhas = int(input())
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
i = 0

while i < quantas_linhas:
    print(alfabeto[i]*(i + 1))
    i += 1
