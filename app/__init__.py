from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__)
    app.config.from_object(os.environ.get('APP_SETTINGS'))

    db.init_app(app)
    migrate.init_app(app)

    return app

