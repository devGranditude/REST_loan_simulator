import unittest
import datetime
from config import constants
from services import datetimeTools

class datetimeToolsTest(unittest.TestCase):

    """test case used to test functions from services.datetimeTools."""

    def test_isSubscribedAfter13th(self):
        date1 = datetime.strptime('2018-01-13', constants.date_format)
        date2 = datetime.strptime('2018-01-14', constants.date_format)
        assert datetimeTools.isSubscribedAfter13th(date1) == False
        assert datetimeTools.isSubscribedAfter13th(date2) == True

    def test_remainingDays(self):
        date = datetime.strptime('2018-01-17', constants.date_format)
        assert datetimeTools.remainingDays(date) == 14

    def test_movetoLastDay(self):
        date = datetime.strptime('2018-01-13', constants.date_format)
        result = datetime.strptime('2018-01-31', constants.date_format)
        assert datetimeTools.movetoLastDay(date) == result

    def test_incrementMonth(self):
        date = datetime.strptime('2018-01-13', constants.date_format)
        result = datetime.strptime('2018-02-13', constants.date_format)
        assert datetimeTools.incrementMonth(date) == result

    def test_movetoLastDayOfNextMonth(self):
        date = datetime.strptime('2018-01-13', constants.date_format)
        result = datetime.strptime('2018-02-28', constants.date_format)
        assert datetimeTools.movetoLastDayOfNextMonth(date) == result