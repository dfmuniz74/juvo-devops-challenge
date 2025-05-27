from behave import given, when, then
import requests

BASE_URL = "https://localhost:4443/score/"

@given('o usuário possui um CPF válido "{cpf}"')
def step_given_cpf_valido(context, cpf):
    context.cpf = cpf

@given('um CPF inexistente "{cpf}"')
def step_given_cpf_inexistente(context, cpf):
    context.cpf = cpf

@given('que um usuário tenta acessar a API via HTTP')
def step_given_http(context):
    context.base_url = "http://localhost:4443/score/"

@when('ele consulta seu score')
def step_when_consulta_score(context):
    base_url = getattr(context, 'base_url', BASE_URL)
    response = requests.get(f"{base_url}{context.cpf}", verify=False)
    context.response = response

@when('ele envia uma requisição insegura')
def step_when_insegura(context):
    response = requests.get("http://localhost:4443/score/33333333333", verify=False)
    context.response = response

@then('a API deve rejeitar a conexão')
def step_then_rejeita(context):
    assert context.response.status_code == 426

@then('retornar um erro informando que "{mensagem}"')
def step_then_https_erro(context, mensagem):
    json_data = context.response.json()
    assert mensagem in json_data['erro']

@then('o status da resposta deve ser {status_code:d}')
def step_then_status_code(context, status_code):
    assert context.response.status_code == status_code

@then('a API deve retornar um score numérico')
def step_then_score_valido(context):
    json_data = context.response.json()
    assert isinstance(json_data['score'], int)
    assert context.response.status_code == 200

@then('a API deve retornar erro "{mensagem}"')
def step_then_erro(context, mensagem):
    json_data = context.response.json()
    assert json_data['erro'] == mensagem
    assert context.response.status_code == 404