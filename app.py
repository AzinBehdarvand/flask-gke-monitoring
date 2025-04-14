from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home page visited")
    return "Hello from GCP Monitoring Demo!"

@app.route("/error")
def error():
    app.logger.error("Something went wrong!")
    return "Error occurred!", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)