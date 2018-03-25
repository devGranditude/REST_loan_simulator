from __future__ import division
import calendar
from config import constants
from dateutil.relativedelta import *

#Check if the loan was subscribed after the 13th
def isSubscribedAfter13th(startDate):
    if startDate.day > constants.limitDay:
        return True
    else:
        return False

#For the loan starting, calculate days remaining until the end of the first month
def remainingDays(date):
    return calendar.monthrange(date.year, date.month)[1] - date.day

#Get the last day of the current month
def movetoLastDay(date):
    lastDayOfCurrentMonth = calendar.monthrange(date.year, date.month)[1]
    return date.replace(day=lastDayOfCurrentMonth)

#Get the next month
def incrementMonth(date):
    return date+relativedelta(months=+1)

#Get the next month of a date
def movetoLastDayOfNextMonth(date):
    nextMonth = incrementMonth(date)
    return movetoLastDay(nextMonth)
