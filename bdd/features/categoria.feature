Feature: Categoria

  Scenario: Criar categoria
    Given o usuario autentica como administrador
    When o usuario cria uma categoria com nome "Casa"
    Then o usuario verifica a categoria criada com sucesso