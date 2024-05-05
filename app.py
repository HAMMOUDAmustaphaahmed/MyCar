from flask import Flask
from flask_jwt_extended import JWTManager
from controllers import blueprint
from models import init_app

app = Flask(__name__)
# Set the JWT secret key
app.config['JWT_SECRET_KEY'] = 'password'


init_app(app)

jwt = JWTManager(app)
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True)
