from config import constants
from schema import LoanSchema, MonthlyPaymentSchema
from config import constants
from datetime import datetime
import calendar

##Set all of monthly payement calculations
##########################################

#Check if the loan was subscribed after the 13th
def isSubscribedAfter13th(startDate):
    if startDate.day > constants.limitDay:
        return True
    else:
        return False

#For the loan starting, calculate days remaining until the end of the first month
def remainingDays(startDate):
    return calendar.monthrange(startDate.year, startDate.month)[1] - startDate.day

#Calculate the monthly interest payment (for remaining days)
def monthlyInterestPayment(daysNumber, interestRate, balance):
    return (daysNumber/constants.yearlyDayNumber) * interestRate * balance

#Calculate the monthly amortization payment
def monthlyAmortizationPayment(balance):
    return constants.amortizationRate * balance

#Check if the outstanding balance is under minimum amortization amount
def isUnderAmortizationMinimum(balance, amortizationMinimum):
    if balance < amortizationMinimum:
        return True
    else:
        return False

# Get the last day of the current month
def movetoLastDay(date):
    lastDayOfCurrentMonth = calendar.monthrange(date.year, date.month)[1]
    return date.replace(day=lastDayOfCurrentMonth)

def incrementMonth(date):
    nextMonth = date.month + 1
    if nextMonth <= 12:
        return date.replace(month=nextMonth)
    else:
        return date.replace(month=1, year=date.year+1)

#Get the next month of a date
def movetoLastDayOfNextMonth(date):
    nextMonth = incrementMonth(date)
    return movetoLastDay(nextMonth)




