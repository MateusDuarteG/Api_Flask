from flask import Flask, jsonify, request

app = Flask(__name__)

agent = [
    {'id': 1, 'Nome': 'Mateus Duarte', 'Matricula': '147884'},
    {'id': 2, 'Nome': 'Pricila Brito', 'Matricula': '1456788'},
    {'id': 3, 'Nome': 'Romeu', 'Matricula': '1456458'}
]


@app.route('/agent', methods=['GET'])
def obter_agent():
    return jsonify(agent)


@app.route('/agent/<int:id>', methods=['GET'])
def obter_agent_id(id):
    for agents in agent:
        if agents.get('id') == id:
            return jsonify(agents)


@app.route('/agent/<int:id>', methods=['PUT'])
def editar_agent_id(id):
    agent_alterado = request.get_json()
    for indice, agents in enumerate(agent):
        if agents.get('id') == id:
            agent[indice].update(agent_alterado)
            return jsonify(agent[indice])


@app.route('/agent', methods=['POST'])
def incluir_novo_agent():
    novo_agents = request.get_json()
    agent.append(novo_agents)
    return jsonify(agent)


@app.route('/agent/<int:id>', methods=['DELETE'])
def excluir_agnt(id):
    for indice, agents in enumerate(agent):
        if agents.get('id') == id:
            del agent[indice]
    return jsonify(agent)


if __name__ == "__main__":
    app.run(debug=True)
