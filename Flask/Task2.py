from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def spoj_seznamy():
    # Generování dvou seznamů s náhodnými čísly
    seznam1 = [random.randint(1, 100) for _ in range(5)]
    seznam2 = [random.randint(1, 100) for _ in range(5)]

    # Spojení dvou seznamů
    vysledek = seznam1 + seznam2

    # Vrácení výsledku jako JSON
    return jsonify({
        'seznam1': seznam1,
        'seznam2': seznam2,
        'spojeny_seznam': vysledek
    })

if __name__ == '__main__':
    app.run(debug=True)
