from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "project": "COVID-19 Info API",
        "author": "Muhammad Rizky - 22523215"
    })

@app.route('/info')
def info():
    return jsonify({
        "symptoms": ["Fever", "Cough", "Fatigue", "Loss of taste/smell"],
        "prevention": ["Wash hands", "Wear mask", "Social distancing"]
    })

if __name__ == '__main__':
    app.run(debug=True)
