from tdd.app.app import Cliente, Pedido, Produto


def test_criar_cliente():
    cliente = Cliente(nome="Vanilton", email="vanilton18@gmail.com")
    assert cliente.nome == "Vanilton"
    assert cliente.email == "vanilton18@gmail.com"


def test_adicionar_produto_ao_pedido():
    pedido = Pedido(cliente=Cliente("Maria", "maria@email.com"))
    produto = Produto(nome="Laptop", preco=1000.00)

    pedido.adicionar_produto(produto, quantidade=2)

    assert len(pedido.itens) == 1
    assert pedido.itens[0].produto == produto
    assert pedido.itens[0].quantidade == 2
