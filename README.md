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


### Using the API

#### 1) Set the environment

All of this project was built under Python 2.7 with the Anaconda packages (available at https://www.anaconda.com/download/). 
You first need to instal virtualenv by the following command:
```
conda install -c anaconda virtualenv
```
Or by the command pip:
```
pip install virtualenv
```

Then, at the project root, create your own virtualenvironment(please keep the same name or update the gitignore file):
```
virtualenv venv_anyfin
```

Now, you need to install flask and flask rest-ful modules into your virtualenv. The first step is to activate your virtualenv...
```
source venv_anyfin/bin/activate
```

... and install flask modules inside
```
pip install Flask
pip install flask-restful
```


The following environment variables need to be setted:
```
export FLASK_APP=app.py
export FLASK_DEBUG=1
```
export FLASK_APP=app.py
export FLASK_DEBUG=1


#### 2) Launch the server

Launch the server from your project root:
```
source venv_anyfin/bin/activate
flask run
```

#### 3) Request /payment_calculator

The goal of this project is to simulate loan by getting main information detail about each monthly payment.
Inputs parameters are sent, and that's the main raison for me to use the /POST route (/GET should receive "payloads").

By default Flask set the localhost url at `http://127.0.0.1:5000/`

Here is the JSON body to be sent (feel free to modify parameters value):
```
{
	"balance": 100000,
	"start_date": "2018-01-14",
	"interest_rate": 0.075,
	"amortization_min": 150
}
```

