from __future__ import division
from schema import LoanSchema, MonthlyPaymentSchema
from config import constants
from datetime import datetime
import calendar
from services import datetimeTools

##Set all of monthly payement calculations
##########################################

#Calculate the monthly interest payment (for remaining days)
def monthlyInterestPayment(date, interestRate, balance):
    daysNumber = datetimeTools.remainingDays(date)
    return (daysNumber/constants.yearlyDayNumber) * interestRate * balance

#Calculate the monthly amortization payment
def monthlyAmortizationPayment(balance, amortizationMin):
    if balance <= amortizationMin:
        return balance
    else:
        return constants.amortizationRate * balance








