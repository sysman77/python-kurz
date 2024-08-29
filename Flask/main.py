from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    print( "Hello World!")
    return "Hello World"


@app.route("/about")
def about():
    return "About section"


if __name__ == "__main__":
    app.run(debug=True)