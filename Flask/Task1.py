from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/")
def home():
    # Vytvoření seznamu náhodných čísel
    seznam = [randint(-10, 10) for _ in range(10)]
    return seznam


if __name__ == "__main__":
    app.run(debug=True)
    