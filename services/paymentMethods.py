from config import constants
from schema import LoanSchema, MonthlyPaymentSchema


##Set all of monthly payement calculations
##########################################

#Check if the loan was subscribed after the 13th
def isSubscribedAfter13th(startingDate):

    pass

#For the loan starting, calculate days remaining until the end of the first month
def remainingDays(startingDate):
    remainingDays = 0
    return remainingDays

#In the case the loan was subscribed after the 13th, calculate debt of interest
def debtOfInterest(remainingDays, interestRate):
    pass

#Calculate the monthly interest payment
def monthlyInterestPayment():
    pass

#Calculate the monthly amortization payment
def monthlyAmortizationPayment():
    pass

#Calculate the total monthly payment
def totalMonthlyPayment():
    pass

#Calculate outstanding balance
def OutstandingBalance():
    pass

#Check if the outstanding balance is under minimum amortization amount
def isUnderAmortizationMinimum(outstandingBalance,amortizationMinimum):
    pass
