from flask import Flask

app = Flask(__name__)

@app.route("/<id>")
def hello(id):
    return "Returned the id: " + str(id)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")