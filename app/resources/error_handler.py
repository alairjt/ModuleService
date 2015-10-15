__author__ = 'alair.tavares'
from app import app
from flask import make_response, jsonify

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Nao Encontrado'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'Erro': 'Nao Permitido'}), 400)

