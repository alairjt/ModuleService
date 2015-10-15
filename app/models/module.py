__author__ = 'alair.tavares'
from app import db

class Module (db.Model):
    id = db.Column(db.Integer, db.Sequence('id_seq'), primary_key=True, nullable=False)
    module = db.Column('module', db.String (20))
    baseUrl = db.Column('baseUrl', db.String(50))
    title = db.Column('title', db.String(50))

    def __init__(self, application, baseUrl, title):
        self.module = application
        self.baseUrl = baseUrl
        self.title = title

    def __repr__(self):
        return '<Module %r>' % self.module

    def as_json(self):
        return dict(
            id = self.id,
            module = self.module,
            baseUrl = self.baseUrl,
            title = self.title)