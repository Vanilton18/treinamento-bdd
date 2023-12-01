"""Autenticacao feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
import pytest
from playwright.sync_api import Playwright, APIRequestContext
from typing import Generator


@scenario('../features/autenticacao.feature', 'Autenticar na solução com falha')
def test_autenticar_na_solucao_com_falha():
    pass


@scenario('../features/autenticacao.feature', 'Autenticar na solução')
def test_autenticar_na_solucao():
    """Autenticar na solução."""
    pass


@given('possuo a url de autenticacao')
def url_auteticacao(api_request_context):
    return api_request_context


@when('informo usuario e senha validos', target_fixture="status_cliente")
def informar_usuario_senha(api_request_context):
    data = {
        "username": "admin",
        "password": "123456"
    }

    cliente = api_request_context.post("/v1/auth/login/", data=data)
    return cliente


@when("informo usuario e senha invalido", target_fixture="status_cliente")
def informar_usuario_senha_invalido(api_request_context):
    data = {
        "username": "admin2",
        "password": "123456"
    }

    cliente = api_request_context.post("/v1/auth/login/", data=data)
    return cliente


@then('usuario autenticado com sucesso')
def verificar_autenticacao(status_cliente):
    assert status_cliente.ok
    assert status_cliente.status == 200


@then('ocorre falha na autenticao')
def verificar_autenticacao_com_falha(status_cliente):
    assert status_cliente.status == 401


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


