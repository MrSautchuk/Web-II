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

from flask import Flask
from rotas import rotas
from paginas import paginas

app = Flask(__name__)

app.register_blueprint(rotas)
app.register_blueprint(paginas)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
