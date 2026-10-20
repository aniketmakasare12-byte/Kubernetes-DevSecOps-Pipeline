from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "DevSecOps Demo Application is Running!"

@app.get("/health")
def health():
    return jsonify(status="healthy")

@app.get("/api/info")
def info():
    return jsonify(
        application="devsecops-demo",
        platform="kubernetes"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)