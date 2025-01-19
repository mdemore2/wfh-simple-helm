import os
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    data = {"data": "Hello World"}
    return jsonify(data), 200


@app.route('/health', methods=['GET'])
def health():
    return "Healthy", 200


@app.route('/secret', methods=['GET'])
def secret():
    return os.environ['MY_SECRET'], 200


@app.route('/env', methods=['GET'])
def env():
    return jsonify(dict(os.environ)), 200


@app.route('/volume', methods=['GET'])
def volume():
    with open('../data/access.txt', 'a+') as f:
        f.write('The volume has been accessed.\n')
        f.seek(0)
        content = f.read()
    return content, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)
