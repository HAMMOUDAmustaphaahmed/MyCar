from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from controllers import login, protected, user, home
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from controllers import blueprint
from database import init_app , test_connection



app = Flask(__name__)
init_app(app)

# Test the database connection
connected, message = test_connection()
if connected:
    print("Database connection:", message)
else:
    print("Database connection:", message)

app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(debug=True)