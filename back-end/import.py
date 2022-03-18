from models.card import CardModel
from models.tag import TagModel
import pandas as pd
from app import app
from db import db

path = input("Write the path of the file. Ex: (C:\Users\<User>\Projetos\cards.csv) ")

df = pd.read_csv(path, index_col=None)
df = df.where(pd.notnull(df), None)

db.init_app(app)

with app.app_context():
    db.create_all()

    for index, row in df.iterrows():
        card = CardModel(texto=row['text'])
        card.save_to_db()

        if row['tag']:
            tags = row['tag'].split(sep=';')

            for tag in tags:
                tag = TagModel(name=tag, card_id=card.id)
                tag.save_to_db()