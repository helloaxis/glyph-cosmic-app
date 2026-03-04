import os
from flask import Flask

app = Flask(name)

@app.route("/")
def home():
    return """
    <h2>Valentine Glyph</h2>
    <form action="/test">
        <input name="date1" placeholder="YYYY-MM-DD" required>
        <input name="date2" placeholder="YYYY-MM-DD" required>
        <button type="submit">Test</button>
    </form>
     """
@app.route("/test")
def test():
    return "FORM WORKS"

if __name__== "__main__":
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
