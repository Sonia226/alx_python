"""
This a module that uses flask as it webframework
"""
from flask import Flask
app = Flask(__name__)

# Define a route for the root URL with strict_slashes=False


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

# Define a route for "/hbnb" with strict_slashes=False


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == '__main__':
    # Run the flask app on 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)