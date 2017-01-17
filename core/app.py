from flask import Flask, jsonify
from flask_restful import Resource, Api
from scraping import Scraping
import json

app = Flask(__name__)
api = Api(app)

class Word_Counter(Resource):
    def get(self):
        quantity = Scraping.count_word("https://docs.python.org/3.5/reference/index.html", "Python")
        word_counted = {}
        word_counted[str("Python")] = quantity
        return jsonify(word_counted)

api.add_resource(Word_Counter, '/word_counter')

if __name__ == "__main__":
    app.run(debug=True)