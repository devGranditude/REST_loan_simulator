# anyfin_assignment

#### Instructions

The goal of this assignment is to create a payment calculator for
flexible loans (i.e. without a predetermined payment period) listing
the monthly payments assuming the customer pays exactly the minimum
required amount each month.

The calculator should provide a command line interface and take basic `
loan information as input as exemplified below (the exact API is up to
you, but all arguments are required).

`payment-calculator --balance 12500 --start-date 2018-03-20 --interest-rate 7.95 --min-amortization-rate 4 --min-amortization 100`

Each monthly minimum payment consists of:


- The interest charge for the number of days in the month (the yearly
nominal interest rate is 7,95% in the example above)

- The amortization, which is the outstanding balance times the minimum
amortization rate (4% in the example above), but at least the minimum
amortization (100 kr in the example above).

Loans starting after the 13th of the month don’t require a payment
until the month after, so in the example above the first required
payment (and amortization) is in April 2018 including a single
amortization charge and interest for 12 + 30 days.

Feel free to use any programming language you like as long as it’s not
too obscure, but make sure the code is well structured and sufficiently
covered by test cases.


### Prerequisites

1) Virtual env + Flask

Python 2.7 Anaconda

conda install -c anaconda virtualenv
At the project root --> virtualenv venv_anyfin
pip install Flask

export FLASK_APP=services/hello_flask.py
export FLASK_DEBUG=1

2) Install MongoDB

3) Install POSTman (or other web client simulator)


### Using

1) Swagger

2) Authentication

3) Payloads



