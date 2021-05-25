from  flask import Flask

from flask_wtf.csrf import CSRFProtect

from blogs.api.models import db
from blogs.api.schemas import ma
from blogs.api.routes import api


def create_app():
    app = Flask(__name__)
    # csrf.init_app(app)
    csrf = CSRFProtect(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SECRET_KEY'] = '0d3d65e6b58a0f464a7d1c8163dd2e8f'

    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()

    csrf.exempt(api)
    app.register_blueprint(api)

    return app
