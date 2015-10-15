__author__ = 'alair.tavares'
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "ModulesService is working"