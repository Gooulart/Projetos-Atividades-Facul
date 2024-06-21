# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 6 alunos)
# ALUNO 1: Gustavo Goulart da Silva
# ALUNO 2: Vinicius Rodrigues Brito Bomfim
# ALUNO 3: Vitor Girão de Lima
# ALUNO 4: Vinicius Ramos da Cunha
# ALUNO 5: Anderson Nunes de Bonoso
# ALUNO 6:

arq = open("notas.txt", "r", encoding="UTF-8")

reprov = []
aprov = []

for i in arq:
    notasProva_sub = []
    AcNotas = []
    listas = []
    listas = i.split(';')
    AcNotas.append(float(listas[2]))
    AcNotas.append(float(listas[3]))
    AcNotas.append(float(listas[4]))
    AcNotas.append(float(listas[5]))
    AcNotas.append(float(listas[6]))

    notasProva_sub.append(float(listas[7]))
    notasProva_sub.append(float(listas[8]))

    AcNotas.sort()
    AcNotas.pop(0)
    notasProva_sub.sort()
    notasProva_sub.pop(0)

    AcMedia = sum(AcNotas)/len(AcNotas)
    media_final = (notasProva_sub[0] + AcMedia) / 2
    faltas = int(listas[-1])

    if media_final >= 6.0 and faltas <= 20:
        aprov.append(listas[1])
    else:
        reprov.append(listas[1])
aprov.sort()
reprov.sort()
arq.close()

reprovados = open("Reprovados.txt", "w", encoding="UTF-8")
aprovados = open("Aprovados.txt", "w", encoding="UTF-8")
reprovados.write('\n'.join(reprov))
aprovados.write('\n'.join(aprov))
