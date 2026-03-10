from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return os.getenv("APP_MESSAGE", "No message set")

@app.route("/health")
def health():
    return os.getenv("APP_HEALTH", "No health status set")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
