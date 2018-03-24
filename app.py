from flask import Flask, request
#from flask.views import MethodView
from flask_restful import Api #, reqparse, abort, Api, Resource
from resources.Loan import Loan

app = Flask(__name__)
api = Api(app)


# Setup the Api resource routing here
api.add_resource(Loan, '/payment_calculator')


if __name__ == '__main__':
    app.run(debug=True)