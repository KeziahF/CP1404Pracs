from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<float:celcius>')
def f(celcius):
    fahrenheit = celcius * 9.0 / 5 + 32
    return str(fahrenheit)


if __name__ == '__main__':
    app.run()
