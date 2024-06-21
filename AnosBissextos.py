def bissexto(ini, fim):
    return i % 4 == 0 and i % 100 != 0 or i % 400 == 0

start = int(input("Insira o ano de início para a contagem: "))
end = int(input("Insira o ano final para a contagem: "))
bi = 0
for i in range(start, end + 1):
    if bissexto (start, end):
        bi += 1
        print(i)

print(f'Quantidade de anos bissextos: {bi}')
