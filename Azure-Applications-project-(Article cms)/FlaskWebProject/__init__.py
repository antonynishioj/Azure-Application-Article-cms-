"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'login'
sess = Session()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configure logging
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    fmt = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
    handler.setFormatter(fmt)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    # Initialize extensions
    db.init_app(app)
    login.init_app(app)
    sess.init_app(app)

    # Import and register routes (if using blueprint)
    from . import views
    if hasattr(views, "bp"):   # if views is a Blueprint
        app.register_blueprint(views.bp)
    else:                      # if views just defines routes
        import FlaskWebProject.views

    return app
