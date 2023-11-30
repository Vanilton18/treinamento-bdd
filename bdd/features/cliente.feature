Feature: Cliente se identificar no ecommerce
  Como cliente de loja
  gostaria de me autenticar
  para realizar compras.

  Scenario: Cliente autenticando na loja
    Given o cliente possui registro na loja
    Then o sistema confirma a autenticidade do cliente


  Scenario: Cliente autenticando
    Given o cliente possui registro atualizado
    Then o sistema confirma a autenticidade do cliente
