from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from controllers import login, protected, user, home
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from controllers import blueprint




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

db = SQLAlchemy(app)
jwt = JWTManager(app)

app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(debug=True)