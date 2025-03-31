from flask import Flask, jsonify, request
from flask_cors import CORS  # Importe o CORS
import csv
import os
import pandas as pd

app = Flask(__name__)
CORS(app)  # Habilita o CORS para todas as rotas

CSV_FILE = 'Dados.csv'

# Função para verificar se o arquivo CSV existe e possui cabeçalhos válidos
def verificar_arquivo_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['nome', 'idade'])  # Cabeçalhos para o CSV
    # Verifica se o CSV tem dados
    try:
        dados = pd.read_csv(CSV_FILE)
    except pd.errors.EmptyDataError:
        # Se o CSV estiver vazio, reescreve os cabeçalhos
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['nome', 'idade'])

# Função para ler dados do CSV
def ler_csv():
    verificar_arquivo_csv()  # Verifica e cria o arquivo caso não exista ou esteja vazio
    try:
        return pd.read_csv(CSV_FILE).to_dict(orient='records')
    except pd.errors.EmptyDataError:
        return []

# Função para escrever dados no CSV
def escrever_csv(dados):
    df = pd.DataFrame(dados)
    df.to_csv(CSV_FILE, index=False)

# Rota para obter os dados
@app.route('/dados', methods=['GET'])
def obter_dados():
    try:
        dados = ler_csv()
        return jsonify(dados)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Rota para adicionar um novo dado
@app.route('/dados', methods=['POST'])
def adicionar_dado():
    try:
        novo_dado = request.json
        dados = ler_csv()
        dados.append(novo_dado)
        escrever_csv(dados)
        return jsonify(novo_dado), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Função para atualizar um dado com base no nome
@app.route('/dados/<nome>', methods=['PUT'])
def atualizar_dado(nome):
    try:
        # Obtenha os dados a partir do corpo da requisição (request)
        novo_dado = request.json
        
        # Leia o CSV e busque o dado pelo nome
        dados = ler_csv()

        # Encontre o dado que corresponde ao nome
        for dado in dados:
            if dado['nome'] == nome:
                dado['idade'] = novo_dado.get('idade', dado['idade'])  # Atualize a idade

        # Reescreva o arquivo CSV com os dados atualizados
        escrever_csv(dados)

        return jsonify({"message": f"Dado de {nome} atualizado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Função para excluir um dado com base no nome
@app.route('/dados/<nome>', methods=['DELETE'])
def excluir_dado(nome):
    try:
        # Leia o CSV e busque o dado pelo nome
        dados = ler_csv()

        # Filtra os dados, removendo o dado com o nome especificado
        dados_filtrados = [dado for dado in dados if dado['nome'] != nome]

        # Se a quantidade de dados não mudou, significa que o nome não foi encontrado
        if len(dados_filtrados) == len(dados):
            return jsonify({"error": f"Dado com nome {nome} não encontrado."}), 404

        # Reescreva o arquivo CSV com os dados restantes
        escrever_csv(dados_filtrados)

        return jsonify({"message": f"Dado de {nome} excluído com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
