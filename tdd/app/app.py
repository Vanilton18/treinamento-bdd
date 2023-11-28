
class Cliente:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Pedido:

    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_produto(self, produto, quantidade):
        self.itens.append(ItemPedido(produto, quantidade))


class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class ItemPedido:

    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
