começo = int(input("Insira o numero de início para a contagem: "))
fim = int(input("Insira o numero final para a contagem: "))
i = 0
def intervalo_primos(inicio, fim, contador):
    for num in range(inicio, fim +1):
        if num >= 2:
            for primos in range(2,num):
                if num % primos == 0:
                    break
            else:
                print(num)
                contador += 1
    print(f'Quantidade de numeros primos: {contador}')
                    

intervalo_primos(começo,fim, i)
