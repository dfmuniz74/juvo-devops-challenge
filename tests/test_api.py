import app

def test_score_valido():
    assert app.consultar_score("33333333333")[1] == 200
    assert isinstance(app.consultar_score("33333333333")[0].json['score'], int)

def test_cpf_invalido():
    assert app.consultar_score("00000000000")[1] == 404
    assert app.consultar_score("00000000000")[0].json['erro'] == "CPF não encontrado"