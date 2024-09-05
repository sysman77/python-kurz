from flask import Flask, render_template
from random import randint

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/random")
def random():
    # Vytvoření seznamu náhodných čísel
    seznam = [randint(-10, 10) for _ in range(10)]
    return render_template("random.html", data=seznam)






if __name__ == "__main__":
    app.run(debug=True, port=8000)