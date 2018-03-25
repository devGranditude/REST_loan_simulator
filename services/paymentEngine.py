from services import paymentMethods
import datetime
from datetime import timedelta
import calendar
import json
from config import constants

def paymentCalculator(balance, start_date, interest_rate, amortization_min):
    #Set list to be used for Json response
    numberPayment_list = []
    outstandingBalance_list = []
    amortizationPayment_list = []
    interestPayment_list = []
    totalPayment_list = []
    datePayment_list = []

    #Set variables
    n = 0
    monthlyPaymentDate = paymentMethods.movetoLastDay(start_date)

    #Calculate debt of interest if needed
    if paymentMethods.isSubscribedAfter13th(start_date):
        remainingDays = paymentMethods.remainingDays(start_date)
        debtOfInterest = paymentMethods.monthlyInterestPayment(remainingDays, interest_rate, balance)

        #And set the first payment date to the end of the next month
        monthlyPaymentDate = paymentMethods.movetoLastDayOfNextMonth(start_date)

    while balance != 0:
        #All days of the current payment month
        daysNumber = calendar.monthrange(monthlyPaymentDate.year, monthlyPaymentDate.month)[1]

        #Set monthly interest payment
        if (debtOfInterest) and n == 0:
            interestPayment = paymentMethods.monthlyInterestPayment(daysNumber, interest_rate, balance) + debtOfInterest
        else:
            interestPayment = paymentMethods.monthlyInterestPayment(daysNumber, interest_rate, balance)

        #Set monthly amortization payment
        if paymentMethods.isUnderAmortizationMinimum(balance, amortization_min):
            amortizationPayment = balance
        else:
            amortizationPayment = paymentMethods.monthlyAmortizationPayment(balance)

        numberPayment_list.append(n)
        outstandingBalance_list.append(balance)
        amortizationPayment_list.append(amortizationPayment)
        interestPayment_list.append(interestPayment)
        totalPayment_list.append(interestPayment + amortizationPayment)
        datePayment_list.append(monthlyPaymentDate.strftime(constants.date_format))

        #Iteration
        monthlyPaymentDate = paymentMethods.incrementMonth(monthlyPaymentDate)
        balance -= amortizationPayment
        n += 1

    answers = {'Payment_number':numberPayment_list, 'outstanding_balance':outstandingBalance_list,
               'amortization':amortizationPayment_list, 'interest':interestPayment_list, 'total_amount':totalPayment_list,
               'date': datePayment_list}

    return json.dumps(answers)