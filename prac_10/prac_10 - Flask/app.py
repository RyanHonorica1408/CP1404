from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f')
@app.route('/f/<celsius>')
def f(celsius=""):
    fahrenheit = C_to_F(celsius)
    return '{}'.format(fahrenheit)


@app.route('/c')
@app.route('/c/<fahrenheit>')
def c(fahrenheit=""):
    celsius = F_to_C(fahrenheit)
    return'{}'.format(celsius)


if __name__ == '__main__':
    app.run()


def C_to_F(celsius):
    celsius = float(celsius)
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def F_to_C(fahrenheit):
    fahrenheit = float(fahrenheit)
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius
