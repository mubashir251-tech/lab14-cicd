from flask import Flask, jsonify
import os
import redis

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True,
    socket_connect_timeout=2,
    socket_timeout=2,
)

@app.route("/")
def index():
    try:
        count = redis_client.incr("request_count")
        return jsonify({
            "name": "Lab14 CI/CD Application",
            "version": os.getenv("APP_VERSION", "1.0.0"),
            "environment": os.getenv("APP_ENV", "development"),
            "request_count": count
        })
    except redis.RedisError:
        return jsonify({"error": "Redis unavailable"}), 503

@app.route("/health")
def health():
    try:
        redis_client.ping()
        return jsonify({"status": "healthy", "redis": "connected"}), 200
    except redis.RedisError:
        return jsonify({"status": "unhealthy", "redis": "disconnected"}), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
