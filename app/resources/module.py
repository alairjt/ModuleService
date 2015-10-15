__author__ = 'alair.tavares'
import json

from flask import jsonify, abort, request, url_for
from app import app
from app.controllers.application import ModuleCtrl
from app.resources import error_handler

@app.route('/api/v1/modules', methods=['GET'])
def get_app():
    return json.dumps([ob.as_json() for ob in ModuleCtrl().get()])

@app.route('/api/v1/modules/<int:module_id>', methods=['GET'])
def get_module_id(module_id):

    module = ModuleCtrl().get_id(module_id)

    if type (module) is str:
        return module

    else:
        return json.dumps(module.as_json())

@app.route('/api/v1/modules', methods=['POST'])
def create_app():
    if not request.json:
        abort(400)

    return json.dumps(ModuleCtrl().create(request.json).as_json())

@app.route('/api/v1/modules/<int:module_id>', methods=['PUT'])
def update_app(module_id):
    modules = ModuleCtrl().update(module_id, request.json)

    if type (modules) is str:
        return modules
    else:
        return json.dumps(modules.as_json())

@app.route('/api/v1/modules/<int:module_id>', methods=['DELETE'])
def delete_app(module_id):
    return ModuleCtrl().delete(module_id)