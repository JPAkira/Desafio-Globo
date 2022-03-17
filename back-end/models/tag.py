from db import db


class TagModel(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'))
    card = db.relationship('CardModel')

    def __init__(self, name, card_id):
        self.name = name
        self.card_id = card_id

    def json(self):
        return {'id': self.id, 'name': self.name, 'card_id':self.card_id}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()