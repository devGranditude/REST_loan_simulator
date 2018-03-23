from flask import Flask
app = Flask(__name__)




#logger.info("AppRouter Init Start")

from router import payment_calculator

@app.route(
    '/payment_calculator',payment_calculator(),

)


def hello_world():
    return 'Hello World, Flask speaking !'