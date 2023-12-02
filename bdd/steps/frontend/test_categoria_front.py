"""Categoria feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)

import utils.database
from playwright.sync_api import expect

@scenario('frontend/categoria.feature', 'Registrar uma categoria')
def test_registrar_uma_categoria():
    """Registrar uma categoria."""
    pass


@given('o usuario acessa a tela de registro de categoria')
def acessar_tela_registro_categoria(page):
    page.goto("http://127.0.0.1:8000/admin/api/category/add/")


@given('o usuario adminstrador está autenticado', target_fixture="page")
def autenticar(browser):
    page = browser
    page.goto("http://127.0.0.1:8000/admin/")
    page.locator("[name=username]").fill("admin")
    page.locator("[name=password]").fill("123456")
    page.get_by_text("Log in").click()
    return page


@when(parsers.parse('o usuario preenche o formulário com {nome:w}, {slug:w}, {is_lux:w}'))
def preencher_formulario(page, nome, slug, is_lux):
    page.locator("[name=name]").fill(nome)
    page.locator("[name=slug]").fill(slug)
    if "sim" == is_lux.lower():
        page.locator("[name=is_lux]").check()

    page.locator("[name=_save]").click()


@then(parsers.parse('o usuario verifica a {nome:w} criada com sucesso'))
def verificar_mensagem_criacao(page, nome):
    assert page.locator(".success").text_content() == f"The category “{nome}” was added successfully."


@given('nao existem categorias cadastradas')
def remove_categoria():
    utils.database.clean_category()
