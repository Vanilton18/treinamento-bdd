from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)


@scenario('argumentos.feature', 'Argumento para os passos given, when, then')
def test_argumento_para_os_passos_given_when_then():
    """Argumento para os passos given, when, then."""
    pass


@given(parsers.parse('há {total:d} laranjas'), target_fixture="saco_laranja")
def ha_laranjas(total):
    return {"total": total, "comida": 0}


@when(parsers.parse('como {comer:d} laranjas'))
def comer_laranja(saco_laranja, comer):
    saco_laranja["comida"] += comer



@then(parsers.parse('deve haver {resultado:d} laranja'))
def verificar_laranjas_restantes_saco(saco_laranja, resultado):
    assert saco_laranja["total"] - saco_laranja["comida"] is resultado


