from schema import LoanSchema
from services import paymentEngine

def read(balance, start_date, interest_rate, amortization_min):
    return paymentEngine.paymentCalculator(balance, start_date, interest_rate, amortization_min)


