from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.card import Card, CardList, CardCreate, CardListFilter
from resources.tag import Tag, TagList, TagCreate

from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'akira'
api = Api(app)
CORS(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(CardCreate, '/card')
api.add_resource(Card, '/card/<int:id>')
api.add_resource(CardList, '/cards')
api.add_resource(CardListFilter, '/cards/<string:tag>')
api.add_resource(TagCreate, '/tag')
api.add_resource(Tag, '/tag/<int:id>')
api.add_resource(TagList, '/tags')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)