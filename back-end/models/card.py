from db import db
from datetime import datetime


class CardModel(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    texto = db.Column(db.String(400))
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    data_modificacao = db.Column(db.DateTime, default=datetime.utcnow)
    tags = db.relationship('TagModel', lazy='dynamic')

    def __init__(self, texto):
        self.texto = texto

    def json(self):
        return {'id': self.id, 'texto': self.texto, 'tags': [tag.json() for tag in self.tags.all()]}

    @classmethod
    def find_by_texto(cls, texto):
        return cls.query.filter_by(texto=texto).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()