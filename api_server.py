from flask import Flask, jsonify, request

api = Flask("API Server")

@api.route('/', methods=['GET'])
def get_root():
    return "Hello from API"

@api.route('/public', methods=['GET'])
def get_public():
    return jsonify({
        "id": 1234,
        "type": "message",
        "data": "Public json message requested and received."
    })

@api.route('/private_basic', methods=['GET'])
def get_private_basic():
    # TODO: Implement basic auth check.
    return "Not yet implemented."

if __name__ == '__main__':
    api.run(debug=True)
