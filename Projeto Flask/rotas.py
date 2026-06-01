# -*- coding: utf-8 -*-
"""
Título: Exercícios Práticos Flask
Descrição: Resolução dos desafios de Rotas Simples, POST, JSON e Templates
Data: 28/04/2026
"""
__author__ = "Allan Sautchuk"
__email__ = "allan.sautchuk@fatec.sp.gov.br"
__turma__ = "DSM - 3º Semestre / Noturno"
__version__ = "1.0.0"

from flask import Blueprint, jsonify, request

rotas = Blueprint('rotas', __name__)

@rotas.route('/message', methods=['GET'])
def message():
    return 'Cadastro Salvo com sucesso'

@rotas.route('/message/<status>', methods=['GET'])
def message_status(status):
    status_map = {
        '200': ('OK: Sucesso geral.', 200),
        '201': ('Created: Sucesso na criação.', 201),
        '400': ('Bad Request: Erro do cliente (sintaxe).', 400),
        '401': ('Unauthorized: Falta autenticação.', 401),
        '404': ('Not Found: Recurso não encontrado.', 404),
        '500': ('Internal Server Error: Erro no servidor.', 500)
    }
    
    if status in status_map:
        return status_map[status]
    return 'Status desconhecido.', 400

@rotas.route('/auth/login', methods=['POST'])
def login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    
    if usuario == 'genivaldo' and senha == 'jerusa':
        return 'OK', 200
    return 'Unauthorized', 401

@rotas.route('/validate_cpf', methods=['POST'])
def validate_cpf():
    data = request.form if request.form else request.get_json(silent=True) or {}
    cpf = data.get('cpf', '')
    
    if cpf and isinstance(cpf, str) and len(cpf.strip()) == 11 and cpf.strip().isdigit():
        return jsonify({'status': 200, 'mensagem': 'CPF Válido'}), 200
    
    return jsonify({'status': 400, 'mensagem': 'Erro do cliente (sintaxe)'}), 400

@rotas.route('/convert/celsius/<float:temp>', methods=['GET'])
def convert_celsius(temp):
    fahrenheit = temp * 1.8 + 32
    return jsonify({
        'celsius': temp,
        'fahrenheit': fahrenheit
    }), 200

@rotas.route('/search', methods=['GET'])
def search():
    q = request.args.get('q')
    if q:
        return f'Você pesquisou por: {q}', 200
    return 'Parâmetro de busca obrigatório', 400

@rotas.route('/api/register', methods=['POST'])
def register():
    data = request.form if request.form else request.get_json(silent=True) or {}
    nome = data.get('nome', '')
    idade = data.get('idade')
    
    try:
        idade = int(idade)
    except (ValueError, TypeError):
        return jsonify({"erro": "Idade inválida"}), 400
        
    if idade < 18:
        return jsonify({"erro": "Cadastro permitido apenas para maiores de idade"}), 403
        
    return f"Usuário {nome} cadastrado", 201

@rotas.route('/products', methods=['GET'])
def products():
    lista_produtos = [
        {'id': 1, 'nome': 'Notebook', 'preco': 3500.00},
        {'id': 2, 'nome': 'Mouse', 'preco': 50.00},
        {'id': 3, 'nome': 'Teclado', 'preco': 150.00}
    ]
    # Se a lista estiver vazia: return '', 204
    if not lista_produtos:
        return '', 204
    return jsonify(lista_produtos), 200

@rotas.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():
    api_key = request.headers.get('X-Api-Key')
    if api_key == 'secret123':
        return 'Acesso ao painel administrativo liberado', 200
    return 'Unauthorized', 401
