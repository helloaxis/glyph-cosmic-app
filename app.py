import os
from flask import Flask

app = Flask(__name__)

def digit_sum(n):
        x = 0
    for c in str(n):
        if c.isdigit():
            x = x + int(c)
    return x

@app.route("/")
def home():
    return "WORKING"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
