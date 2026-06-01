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

from flask import Blueprint, render_template

paginas = Blueprint('paginas', __name__, template_folder='templates')

@paginas.route('/')
@paginas.route('/home')
def home():
    return render_template('index.html', title='Home - Desafios Flask')
