
from flask_restful import Resource, Api

class FizzBuzz(Resource):
    def get(self,number):
        if int(number) % 3 == 0 and int(number) % 5 == 0:
            return "fizzbuzz"
        elif int(number) % 3 == 0:
            return "fizz"
        elif int(number) % 5 == 0:
            return "buzz"
        else:
            return number

class FizzBuzzCode(Resource):
    def get(self):
        line1 = "if int(number) % 3 == 0 and int(number) % 5 == 0:"
        line2 = "return fizzbuzz"
        return line1+" "+ line2