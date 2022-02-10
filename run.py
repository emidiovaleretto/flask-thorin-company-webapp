import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, World!</h1>"

if __name__ == "__main__":
    app.run(
        host="localhost",
        port=int(os.environ.get("PORT", "8000")),
        debug=True
    )