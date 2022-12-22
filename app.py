from flask import Flask

app = Flask(__name__)

@app.route("/<id>")
def getID(id):
    return "Returned the id: " + str(id)

@app.route("/")
def hello():
    return "Hello world"
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")