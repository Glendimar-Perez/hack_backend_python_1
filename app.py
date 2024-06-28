from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/users', methods=['GET'])
def get():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['POST'])
def create():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['DELETE'])
def delete():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['PUT'])
def update():
    return jsonify({'payload': 'success'})

@app.route('/api/v1/users', methods=['GET'])
def api_get():
    return jsonify({'payload': []})

@app.route('/api/v1/user', methods=['POST'])
def api_create():
    email = request.args.get('email')
    name = request.args.get('name')
    return jsonify({'payload': {'email': email, 'name': name}})

@app.route('/api/v1/user/add', methods=['POST'])
def api_create_form():
    email = request.form.get('email')
    name = request.form.get('name')

    id = request.form.get('id')
    return jsonify({
        'payload': {
            'email': email,
            'name': name,
            'id': id
        }
    })

@app.route('/api/v1/user/create', methods=['POST'])
def api_create_json():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    id = data.get('id')
    return jsonify({
        'payload': {
            'email': email,
            'name': name,
            'id': id
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
