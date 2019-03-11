from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from flask_cors import CORS


app = Flask(__name__, static_folder='http')
CORS(app)
api = Api(app)


class FizzBuzz(Resource):
    def get(self):

        return "Yay. I can return something upon pressing a button"



api.add_resource(FizzBuzz, '/fizz-buzz')  # Route_1

if __name__ == '__main__':
    app.run(port='5002')

# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def fizzBuzz():
#     return "number"
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
