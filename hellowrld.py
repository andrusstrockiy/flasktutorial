from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world from chapter 1"


if __name__ == '__main__':
    app.run(port=5000,debug=True)