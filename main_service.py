from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello AI! CI/CD 流程已闭环！"

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "version": "1.0.0"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)