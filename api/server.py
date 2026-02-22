from flask import Flask, jsonify, request
import api.data as data

api = Flask(__name__)

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

@api.route('/users', methods=['GET'])
def get_users():
    return jsonify(data.users)

@api.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    return f"User ID: {user_id}"

@api.route('/items', methods=['GET', 'POST'])
def handle_items():
    if request.method == 'GET':
        #return f"Some list of items"
        return jsonify(data.items)
    elif request.method == 'POST':
        return f"New item added"
    return None

if __name__ == '__main__':
    api.run(debug=True)
