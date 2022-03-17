from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.tag import TagModel


class Tag(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('card_id',
                        type=int,
                        required=True,
                        help="Every tag needs a card object."
                        )

    
    def get(self, id):
        tag = TagModel.find_by_id(id)
        if tag:
            return tag.json()
        return {'message': 'Item not found'}, 404

    @jwt_required()
    def delete(self, id):
        tag = TagModel.find_by_id(id)
        if tag:
            tag.delete_from_db()
            return {'message': 'Tag deleted successful!'}
        return {'message': 'Tag not found.'}, 404
        
    @jwt_required()
    def put(self, id):
        data = Tag.parser.parse_args()

        tag = TagModel.find_by_id(id)

        if tag:
            tag.name = data['name']
            tag.card_id = data['card_id']
        else:
            item = TagModel(id, **data)

        tag.save_to_db()

        return tag.json()

class TagCreate(Resource):
    @jwt_required()
    def post(self):
        data = Tag.parser.parse_args()

        tag = TagModel(**data)

        try:
            tag.save_to_db()
        except:
            return {"message": "An error occurred inserting the tag."}, 500

        return tag.json(), 201

class TagList(Resource):
    def get(self):
        return {'tags': list(map(lambda x: x.json(), TagModel.query.all()))}