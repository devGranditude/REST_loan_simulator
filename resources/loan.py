from flask_restful import Resource
#from controller import loanRestController

class Loan(Resource):

    def get(self):
        return "Not yet developped. This will be used to list all persisted loans"

    def post(self, balance=None, start_date=None,interest_rate=None, amortization_min=None):
        return {'hello': 'Flask is speaking'}

    def put(self):
        return "Not yet developped. This will be used to update/create persisted loans"

    def delete(self):
        return "Not yet developped. This will be used to delete persisted loans"