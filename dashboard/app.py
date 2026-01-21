from flask import Flask, render_template
import json

app = Flask(__name__)
LOG_FILE = "../logs/blocked_ips.json"

@app.route("/")
def index():
    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []
    return render_template("index.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
