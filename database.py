from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError

# Initialize SQLAlchemy
db = SQLAlchemy()

def init_app(app):
    # Configure MySQL connection URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/mycar'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable SQLAlchemy modification tracking
    # Initialize SQLAlchemy with the Flask app
    db.init_app(app)


def test_connection():
    try:
        # Attempt to connect to the database
        db.create_all()
        return True, "Connected successfully"
    except OperationalError as e:
        # Connection failed
        return False, f"Failed to connect: {str(e)}"