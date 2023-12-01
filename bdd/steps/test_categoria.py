from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)
import pytest
from playwright.sync_api import Playwright, APIRequestContext
from typing import Generator
import utils.database

@pytest.fixture(scope="session")
def api_request_context(
        playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    headers = {
        "Content-Type": "application/json"
    }
    request_context = playwright.request.new_context(
        base_url="http://127.0.0.1:8000/", extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()


@scenario('categoria.feature', 'Criar categoria')
def test_criar_categoria():
    """Criar categoria."""
    pass


@given('o usuario autentica como administrador', target_fixture="token")
def autenticar_como_administador(api_request_context):
    data = {
        "username": "admin",
        "password": "123456"
    }
    token = api_request_context.post("/v1/auth/login/", data=data).json()['access']
    return token


@when(parsers.parse('o usuario cria uma categoria com nome "{categoria:w}"'), target_fixture="categoria_criada")
def criar_categoria(api_request_context, token, categoria):
    headers = {
        "Authorization": "Bearer " + token
    }
    data = {
        "name": categoria,
        "slug":  "categoria",
        "is_lux": True
        }
    categoria_criada = api_request_context.post("/v1/api/category/", data=data, headers=headers)
    return categoria_criada


@then('o usuario verifica a categoria criada com sucesso')
def verificar_categoria(categoria_criada):
    assert categoria_criada.ok
    assert categoria_criada.status == 201


@given('nao existem categorias cadastradas')
def remove_categoria():
    utils.database.clean_category()

