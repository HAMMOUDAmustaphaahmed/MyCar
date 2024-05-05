from flask import Flask
from controllers import blueprint
from models import init_app

app = Flask(__name__)
init_app(app)

app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True)
