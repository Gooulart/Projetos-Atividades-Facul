class Endereco:
    def __init__(self, rua, numero, complemento, bairro, cidade, uf, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep


class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco


class Pedido:
    def __init__(self, cliente, altura, largura, frase, cor_placa, cor_letra):
        self.cliente = cliente
        self.altura = altura
        self.largura = largura
        self.frase = frase
        self.cor_placa = cor_placa
        self.cor_letra = cor_letra
        self.valor_fixo_material = 147.00
        self.valor_fixo_letra = 0.35

    def calcular_total(self):
        area = self.altura * self.largura
        custo_material = area * self.valor_fixo_material
        custo_desenho = len(self.frase.replace(" ", "")) * \
            self.valor_fixo_letra
        valor_final = custo_material + custo_desenho
        return valor_final


class Historico:
    def __init__(self):
        self.pedidos = []

    def inserir_pedido(self, pedido):
        self.pedidos.append(pedido)

    def calcular_faturamento(self):
        soma = 0
        for i in self.pedidos:
            soma += i.calcular_total()
        return soma
