from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Word_Counter(Resource):
    def get(self):
        return {"status": "Construction"}

api.add_resource(Word_Counter, '/word_counter')

if __name__ == "__main__":
    app.run(debug=True)