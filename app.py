from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "service": "devops-demo-api"}), 200

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "CI/CD & Terraform automated pipeline active"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)