Feature: Autenticacao


  Scenario: Autenticar na solução
    Given possuo a url de autenticacao
    When informo usuario e senha validos
    Then usuario autenticado com sucesso

  Scenario: Autenticar na solução com falha
    Given possuo a url de autenticacao
    When informo usuario e senha invalido
    Then ocorre falha na autenticao