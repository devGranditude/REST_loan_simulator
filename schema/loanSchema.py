from flask_restful import fields
from schema import MonthlyPaymentSchema

class LoanSchema(object):
    #balance = fields.Float()
    #startingDate = fields.DateTime()
    #yearlyInterestRate = fields.Float()
    #amortizationMinimum = fields.Float()
    payment = fields.Nested(MonthlyPaymentSchema)