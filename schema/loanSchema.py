from flask_restful import fields, marshal_with

from schema import MonthlyPaymentSchema

class LoanSchema(object):
    #balance = fields.Float()
    #startingDate = fields.DateTime()
    #yearlyInterestRate = fields.Float()
    #amortizationMinimum = fields.Float()
    payment = fields.Nested(MonthlyPaymentSchema, many=True)
