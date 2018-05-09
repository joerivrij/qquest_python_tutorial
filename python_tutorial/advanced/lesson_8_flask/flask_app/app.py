from flask import Flask, render_template, jsonify, request
import json

GLOBAL_ID = 1
GLOBAL_USERS = []

class User():
    def __init__(self, name):
        self.id = GLOBAL_ID
        self.name = name


def return_user(id):
    for user in GLOBAL_USERS:
        if user.id == id:
            json_user = user.__dict__
            return json_user


def add_user(user):
    global GLOBAL_ID, GLOBAL_USERS
    GLOBAL_USERS.append(user)
    GLOBAL_ID += 1


app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

@app.route('/users', methods=['GET'])
def get_all_users():
    users = []
    for user in GLOBAL_USERS:
        json_user = user.__dict__
        users.append(json_user)
    return json.dumps(users, indent=4)


@app.route('/users/<id>', methods=['GET'])
def get_user_by_id(id):
    user = return_user(int(id))
    return json.dumps(user, indent=4)


@app.route('/users', methods=['POST'])
def create_a_new_user():
    json_body = request.json
    new_user = User(json_body['name'])
    add_user(new_user)
    return json.dumps(new_user.__dict__, indent=4)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')


if __name__ == '__main__':
    Jim = User("Jim")
    add_user(Jim)
    app.run()

