from controller import LoanRestController
from flask import request
from flask_restful import Resource, abort, reqparse
from config import constants
from datetime import datetime


class Loan(Resource):
    def get(self):
        abort(http_status_code=404, errors='Not yet developed. This will be used to list all persisted loans')

    def post(self):
        controller = eval(self.__class__.__name__ + "RestController")

        #Implement the request parser
        parser = reqparse.RequestParser()
        parser.add_argument('balance', type=float)
        parser.add_argument('start_date', type=str)
        parser.add_argument('interest_rate', type=float)
        parser.add_argument('amortization_min', type=float)
        args = parser.parse_args()

        #Parse all data contained into the request
        balance = args['balance']
        start_date = datetime.strptime(args['start_date'], constants.date_format)
        interest_rate = args['interest_rate']
        amortization_min = args['amortization_min']

        if None in (balance,start_date,interest_rate, amortization_min):
            abort(http_status_code=404, errors='At least one of your inputs arguments is missing. \'balance\', \'start_date\','
             '\'interest_rate\' and \'amortization_min\' are expected over Json format')
        else:
            try:
                return controller.read(balance, start_date, interest_rate, amortization_min), 200
            except Exception as e:
                abort(http_status_code=500, errors='{}'.format(e))

    def put(self):
        abort(http_status_code=404, errors='Not yet developed. This will be used to update/create persisted loans')

    def delete(self):
        abort(http_status_code=404, errors='Not yet developed. This will be used to delete persisted loans')

# @TODO: remove automated message added by abort like "You have requested blabla.." --> set ERROR_404_HELP to False in the app config
# --> https://github.com/flask-restful/flask-restful/blob/0.3.3/flask_restful/__init__.py#L301

