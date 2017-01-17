from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from scraping import Scraping
import json

app = Flask(__name__)
api = Api(app)

class Word_Counter(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str)
        parser.add_argument('word', type=str)
        args = parser.parse_args()

        url = args.get('url')
        word = args.get('word')

        quantity = Scraping.count_word(url, word)
        word_counted = {}
        word_counted[str(word)] = quantity
        return jsonify(word_counted)

api.add_resource(Word_Counter, '/word_counter')

if __name__ == "__main__":
    app.run(debug=True)