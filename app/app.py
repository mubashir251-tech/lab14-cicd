from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "name": "Lab14 CI/CD Application",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("APP_ENV", "development")
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
