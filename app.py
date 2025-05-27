from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/score/<cpf>', methods=['GET'])
def consultar_score(cpf):
    """
    Simula uma resposta de consulta de score de crédito para alguns CPFs fictícios.
    O CPF deve ser passado como parte da URL.
    """
    # Scores fictícios
    scores = {
        '12345678901': 750,
        '98765432109': 620,
        '33333333333': 906
    }

    score = scores.get(cpf, None)
    
    if score is not None:
        resposta = jsonify({'cpf': cpf, 'score': score})
        codigo = 200
    else:
        resposta = jsonify({'erro': 'CPF não encontrado'})
        codigo = 404
    
    return resposta, codigo

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, ssl_context=('cert.pem', 'key.pem'))