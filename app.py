from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from resources.loan import Loan

app = Flask(__name__)
api = Api(app)


# Setup the Api resource routing here
api.add_resource(Loan, '/payment_calculator')


if __name__ == '__main__':
    app.run(debug=True)