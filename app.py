from flask import Flask
import os
app = Flask(__name__)


@app.route("/")
def home():
    return f"<h1>Welcome to flask app.</h1> You are connected to {os.uname()[1]}"+"\n"


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=9632)
