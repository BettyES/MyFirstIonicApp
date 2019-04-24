from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from fizzbuzz import FizzBuzz, FizzBuzzCode



app = Flask(__name__, static_folder='http')
CORS(app)
api = Api(app)


api.add_resource(FizzBuzz, '/fizz-buzz/<number>')  # Route_1
api.add_resource(FizzBuzzCode, '/fizz-buzz/code')

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
