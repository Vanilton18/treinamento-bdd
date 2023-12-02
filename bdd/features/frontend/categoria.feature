Feature: Categoria

  Background:
    Given o usuario adminstrador está autenticado
    And nao existem categorias cadastradas

  Scenario Outline: Registrar uma categoria
    Given o usuario acessa a tela de registro de categoria
    When o usuario preenche o formulário com <nome>, <slug>, <is_lux>
    Then o usuario verifica a <nome> criada com sucesso

    Examples:
    | nome | slug | is_lux |
    |  Casa   |  casa    |  sim       |
    |  Automotivo   |  automotivo    |  não       |

