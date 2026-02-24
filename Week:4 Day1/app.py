from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask, Welcome to Axilex Services Private ltd !"

if __name__ == "__main__":
    app.run(debug=True)
