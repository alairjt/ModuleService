__author__ = 'alair.tavares'

from app.models.module import Module
from app import db

class ModuleCtrl():
    def get(self):
        applications = Module.query.all()
        return applications

    def get_id(self, id):
        application = Module.query.filter_by(id=id).one()
        if(application):
            return application
        else:
            return "Registro nao encontrado"

    def create(self, obj):
        module = Module(
            obj['application'],
            obj['baseUrl'],
            obj['title']
        )

        db.session.add(module)
        db.session.commit()
        return module

    def update(self, id, obj):
        application = Module.query.filter_by(id=id).first()

        if(application):
            db.session.query(Module).filter(Module.id == id).update(obj)
            db.session.commit()
            return application
        else:
            return "Registro nao encontrado"

    def delete(self, id):
        application = Module.query.filter_by(id=id).one()

        if(application):
            db.session.query(Module).filter(Module.id == id).delete()
            db.session.commit()
            return "Registro apagado"
        else:
            return "Registro nao encontrado"