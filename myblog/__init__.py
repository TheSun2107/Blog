import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
bootstrap = Bootstrap()
moment = Moment()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
 
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)


    from myblog.main import bp as main_bp
    app.register_blueprint(main_bp)

    from myblog.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from myblog.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from myblog.posts import bp as posts_bp
    app.register_blueprint(posts_bp)

    return  app

from myblog import models