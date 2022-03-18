from operator import contains
from flask_restful import Resource, reqparse
from models.card import CardModel
from models.tag import TagModel
from flask_restful import inputs
from flask_jwt import jwt_required
from datetime import datetime

class Card(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('texto',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )


    def get(self, id):
        card = CardModel.find_by_id(id)
        if card:
            return card.json()
        return {'message': 'Card not found'}, 404

    @jwt_required()
    def delete(self, id):
        card = CardModel.find_by_id(id)
        if card:
            card.delete_from_db()

        return {'message': 'Card deleted'}
    @jwt_required()
    def put(self, id):
        data = Card.parser.parse_args()

        card = CardModel.find_by_id(id)

        if card:
            card.texto = data['texto']
            card.data_modificacao = datetime.now()
            code = 200
        else:
            card = CardModel(**data)
            code = 201

        card.save_to_db()

        return card.json(), code

class CardCreate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('texto',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('tags',
                        type=str,
                        required=False,
                        action='append'
                        )

    def post(self):
        data = Card.parser.parse_args()

        card = CardModel(texto=data['texto'])
        try:
            card.save_to_db()
        except:
            return {"message": "An error occurred creating the card."}, 500
        
        for item in self.parser.parse_args()['tags']:
            tag = TagModel(name=item, card_id=card.id)
            try:
                tag.save_to_db()
            except:
                return {"message": "An error occurred creating the tags."}

        return card.json(), 201


class CardList(Resource):
    def get(self):
        return {'cards': list(map(lambda x: x.json(), CardModel.query.all()))}

class CardListFilter(Resource):
    def get(self, tag):
        return {'cards': list(map(lambda x: x.json(), CardModel.query.filter(CardModel.tags.any(name=tag))))}
