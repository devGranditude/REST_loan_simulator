from services import paymentMethods
from services import datetimeTools
import datetime
from datetime import timedelta
import calendar
import json
from config import constants
import pandas as pd
from flask import jsonify

def paymentCalculator(balance, start_date, interest_rate, amortization_min):
    #Initialization
    n = 0
    paymentDate = datetimeTools.movetoLastDay(start_date)
    data = []
    debt0fInterest = 0

    #If loan is subscribed after 13th of the first of month
    if datetimeTools.isSubscribedAfter13th(start_date):
        debt0fInterest = paymentMethods.monthlyInterestPayment(start_date, interest_rate, balance)
        paymentDate = datetimeTools.movetoLastDayOfNextMonth(start_date)

    while balance != 0:

        amortizationPayment = paymentMethods.monthlyAmortizationPayment(balance, amortization_min)
        interestPayment = paymentMethods.monthlyInterestPayment(paymentDate,interest_rate,balance) + debt0fInterest

        item = {
                'payment_number': n,
                'balance': balance,
                'amortization': amortizationPayment,
                'interest': interestPayment,
                'total_amount_to_pay': amortizationPayment + interestPayment,
                'payment_date': paymentDate.strftime(constants.date_format)
                }

        data.append(item)

        # Iteration
        debt0fInterest = 0
        paymentDate = datetimeTools.incrementMonth(paymentDate)
        balance = balance - amortizationPayment
        n += 1

    json_string =  json.dumps(data, sort_keys=True,indent=4)
    return json.loads(json_string)
