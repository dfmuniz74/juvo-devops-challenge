Feature: API de Score de Crédito

  Como um sistema de análise de crédito
  Quero consultar o score de um usuário pelo CPF
  Para fornecer informações financeiras relevantes de forma segura, escalável e confiável

  Scenario: Requisição via HTTPS obrigatória
    Given que um usuário tenta acessar a API via HTTP
    When ele envia uma requisição insegura
    Then a API deve rejeitar a conexão
    And retornar um erro informando que "Apenas HTTPS é permitido"
    And o status da resposta deve ser 426 (Upgrade Required)
    
  Scenario: Score válido para CPF existente
    Given o usuário possui um CPF válido "33333333333"
    When ele consulta seu score
    Then a API deve retornar um score numérico
    And o status da resposta deve ser 200

  Scenario: CPF inexistente
    Given um CPF inexistente "00000000000"
    When ele consulta seu score
    Then a API deve retornar erro "CPF não encontrado"
    And o status da resposta deve ser 404 (Not Found)