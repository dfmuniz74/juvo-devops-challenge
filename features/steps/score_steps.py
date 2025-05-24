from behave import given, when, then
import requests

BASE_URL = "http://localhost:5000/score/"

@given('o usuário possui um CPF válido "{cpf}"')
def step_given_cpf_valido(context, cpf):
    context.cpf = cpf

@given('um CPF inexistente "{cpf}"')
def step_given_cpf_inexistente(context, cpf):
    context.cpf = cpf

@when('ele consulta seu score')
def step_when_consulta_score(context):
    response = requests.get(f"{BASE_URL}{context.cpf}")
    context.response = response

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

@then('o status da resposta deve ser {status_code:d}')
def step_then_status_code(context, status_code):
    assert context.response.status_code == status_code