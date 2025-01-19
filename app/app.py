import os
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def helloworld():
    if (request.method == 'GET'):
        data = {"data": "Hello World"}
        return jsonify(data), 200


@app.route('/', methods=['GET'])
def index():
    return "Healthy", 200


@app.route('/secret', methods=['GET'])
def secret():
    return os.environ['MY_SECRET'], 200


@app.route('/env', methods=['GET'])
def env():
    return jsonify(dict(os.environ)), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)
