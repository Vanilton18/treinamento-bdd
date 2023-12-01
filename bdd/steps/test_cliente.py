import pytest
from pytest_bdd import scenario, given, when, then
from tdd.app.app import Cliente


#@pytest.fixture
#def cliente():
#    cliente = Cliente(nome="Vanilton", email="vanilton18@gmail.com")
#    return cliente


@scenario('cliente.feature', 'Cliente autenticando')
def test_cliente_autenticando():
    pass

@scenario('cliente.feature', 'Cliente autenticando na loja')
def test_cliente_autenticando_na_loja():
    """Cliente autenticando na loja."""
    pass


@given("o cliente possui registro atualizado", target_fixture="cliente")
@given("o cliente possui registro na loja", target_fixture="cliente")
def o_cliente_possui_registro_loja():
    cliente = Cliente(nome="Vanilton", email="vanilton18@gmail.com")
    return cliente


@then('o sistema confirma a autenticidade do cliente')
def verificar_autenticidade_cliente(cliente):
    assert cliente.nome is "Vanilton"
    assert cliente.email is "vanilton18@gmail.com"
