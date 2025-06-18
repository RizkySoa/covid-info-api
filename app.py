from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "<h1>Hello from Muhammad Rizky, 22523215!</h1>"

if __name__ == '__main__':
    app.run()
