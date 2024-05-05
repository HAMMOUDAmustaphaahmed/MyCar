from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User, Car

blueprint = Blueprint('controllers', __name__)

# Your existing routes
@blueprint.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@blueprint.route('/home', methods=['GET'])
def index():
    return render_template('index.html')

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token)
        else:
            return jsonify({'msg': 'Bad username or password'}), 401
    else:
        return render_template('login.html')

@blueprint.route('/logout')
def logout():
    # Clear session data or perform any logout action
    return redirect(url_for('controllers.home'))

# Your existing protected and user routes
@blueprint.route('/protected')
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({"message": "Hello, {}".format(user.username)}), 200

@blueprint.route('/user')
@jwt_required()
def user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    cars = Car.query.filter_by(user_id=user_id).all()
    return jsonify({"user": {"username": user.username, "cars": [{"make": car.make, "model": car.model, "year": car.year} for car in cars]}}), 200
