from flask import Flask

app = Flask(__name__)

@app.route("/")
def grettings():
    return "Hello my friend!"

@app.route("/about")
def about():
    return "About this project: "

if __name__ == "__main__":
    app.run(debug=True)

