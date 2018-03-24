from flask_restful import fields, marshal_with

class MonthlyPaymentSchema(object):
    number = fields.Integer()
    outstandingBalance = fields.Float()
    interestPayment = fields.Float()
    amortizationPayment = fields.Float()
    totalMonthlyPayment = fields.Float()
    #date = fields.DateTime()