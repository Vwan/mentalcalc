
from api.utils import load_json_file
from flask import Flask
from config import load_config
from flask_sqlalchemy import SQLAlchemy

config_name = "DEVELOPMENT"

# def create_app(config_name):
app = Flask(__name__)
config = load_config(config_name)
app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

with app.app_context():
    from controller import blueprint_views
    for blueprint_view in blueprint_views:
        app.register_blueprint(blueprint_view)
    # return app

