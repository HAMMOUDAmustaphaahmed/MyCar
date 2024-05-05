from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, User, Car

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

# Route for user registration
@blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
         # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'msg': 'User created successfully'}), 201
    elif request.method == 'POST':
        return jsonify({'msg': 'Missing username or password'}), 400
    return render_template('signup.html')


