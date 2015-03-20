from flask import Flask, render_template
from flask import current_app as app
from . import models
from .extensions import db, migrate, config, mail
from .views import stripe_practice


SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/stripe_practice.db"
DEBUG = True
SECRET_KEY = 'development-key'


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    app.register_blueprint(stripe_practice)
    app.config.from_pyfile('keys.cfg')
    app.config['SITE'] = 'https://connect.stripe.com'
    app.config['AUTHORIZE_URI'] = '/oauth/authorize'
    app.config['TOKEN_URI'] = '/oauth/token'
    app.config['MAIL_SERVER']
    app.config['MAIL_PORT']
    app.config['MAIL_USE_TLS']
    app.config['MAIL_USE_SSL']
    app.config['MAIL_USERNAME']
    app.config['MAIL_PASSWORD']
    config.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    return app
