Feature: Exemplo com tabela

    Scenario Outline: Comer laranjas com argumento tabulados
        Given há <total> laranjas
        When como <comer> laranjas
        Then deve haver <restante> laranja

        Examples:
        | total | comer | restante |
        |  12   |  5    |  5       |
        |  50   |  10    |  40     |
        |  50   |  42    |  8     |
        |  10   |  10    |  0     |
        |  50   |  10    |  43     |
