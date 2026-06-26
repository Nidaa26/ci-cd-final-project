"""Flask microservice for the CI/CD final project."""
import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """Root endpoint returning a welcome message."""
    return jsonify(message="Welcome to the CI/CD Final Project service"), 200


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint used by readiness and liveness probes."""
    return jsonify(status="OK"), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print("SERVICERUNNING")
    app.run(host="0.0.0.0", port=port)
