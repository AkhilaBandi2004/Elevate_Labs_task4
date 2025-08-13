from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    1: {'name': 'Akbar', 'email': 'akbar@example.com'},
    2: {'name': 'Birbal', 'email': 'birbal@example.com'}
}
next_user_id = 3

@app.route('/users', methods=['GET'])
def get_users():
    """Returns a list of all users."""
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Returns a single user if found, otherwise a 404 error."""
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    """Creates a new user."""
    global next_user_id
    if not request.json or 'name' not in request.json or 'email' not in request.json:
        return jsonify({'error': 'Missing name or email in request body'}), 400

    new_user = {
        'name': request.json['name'],
        'email': request.json['email']
    }
    
    users[next_user_id] = new_user
    new_user_id = next_user_id
    next_user_id += 1
    
    response_data = {'id': new_user_id, 'data': new_user}
    return jsonify(response_data), 201 

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Updates an existing user's information."""
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    if not request.json:
        return jsonify({'error': 'Request body cannot be empty'}), 400

    users[user_id].update(request.json)
    
    return jsonify(users[user_id])

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Deletes a user."""
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    del users[user_id]
    return jsonify({'result': f'User {user_id} deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
