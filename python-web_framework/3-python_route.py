"""
This a module that uses flask as it webframework
"""
from flask import Flask
import re
app = Flask(__name__)

# Define a route for the root URL with strict_slashes=False


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

# Define a route for "/hbnb" with strict_slashes=False


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

# Define a route for "/c/<text>" with strict_slashes=False


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscores (_) with spaces in the text
    text = re.sub(r'_', ' ', text)
    return "C {}".format(text)

# Define a route for "/python/<text>" with strict_slashes=False


@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    # Replace underscores (_) with spaces in the text
    text = re.sub(r'_', ' ', text)
    return "Python {}".format(text)


if __name__ == '__main__':
    # Run the flask app on 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)